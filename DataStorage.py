import sqlite3

DATABASE_NAME = 'SpeedTestResults.db'


def testDataBaseConnection():
    try:
        connection = sqlite3.connect(DATABASE_NAME)
    except sqlite3.DatabaseError as e:
        print('Connection failed:', e)
    else:
        print('Connection established..')
    finally:
        connection.close()


if __name__ == '__main__':
    print('Testing database connection..')
    testDataBaseConnection()
