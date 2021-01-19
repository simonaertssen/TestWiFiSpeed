from sqlite3 import connect, DatabaseError

DATABASE_NAME = 'SpeedTestResults.db'

def SafeDataBaseConnection():
    try:
        connection = connect(DATABASE_NAME)
    except DatabaseError as e:
        connection.close()
        raise
    return connection

def DisconnectDataBase(connection):
    try:
        connection.close()
    except DatabaseError as e:
        raise

def ExecuteDataBaseCommands(commands):
    connection = SafeDataBaseConnection()
    if not isinstance(commands, list):
        commands = [commands]
    try:
        for command in commands:
            connection.execute(command)
        connection.commit()
    except DatabaseError as e:
        raise
    finally:
        DisconnectDataBase(connection)

def CreateTableCommand(table_name):
    return f"CREATE TABLE IF NOT EXISTS {table_name} (TIMESTAMP TEXT NOT NULL, DOWNLOADSPEED REAL, UPLOADSPEED REAL, LATENCY REAL);"

def AddResultsToDataBaseTable(table_name, results):
    tableCommand = CreateTableCommand(table_name)
    TIMESTAMP = results["TIMESTAMP"]
    DOWNLOADSPEED = results["DOWNLOADSPEED"]
    UPLOADSPEED = results["UPLOADSPEED"]
    LATENCY = results["LATENCY"]
    addCommand = f"INSERT INTO {table_name} (TIMESTAMP,DOWNLOADSPEED,UPLOADSPEED,LATENCY) VALUES ({TIMESTAMP},{DOWNLOADSPEED},{UPLOADSPEED},{LATENCY});"
    ExecuteDataBaseCommands([tableCommand, addCommand])

def GetTableContents(table_name):
    tableRows = []
    with SafeDataBaseConnection() as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(f"SELECT * FROM {table_name}")
            tableRows = cursor.fetchall()
            connection.commit()
        except DatabaseError as e:
            print("Database error:", e)
    return tableRows

def TestDataBaseConnection():
    try:
        DisconnectDataBase(SafeDataBaseConnection())
    except DatabaseError as e:
        print('Test failed:', e)
    else:
        print('Test succeeded...')

if __name__ == '__main__':
    print('Testing database connection..')
    TestDataBaseConnection()

    tableName = "TestTable"
    results = {"TIMESTAMP": "0001", "DOWNLOADSPEED": 3.14, "UPLOADSPEED": 1.61, "LATENCY": 12.0}
    AddResultsToDataBaseTable(tableName, results)

    contents = GetTableContents(tableName)
    for row in contents:
        print(row)
