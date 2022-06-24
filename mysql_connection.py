import mysql.connector

def get_connection() :
    connection = mysql.connector.connect(
            host = 'yhdb.c8nbdutl9vtz.ap-northeast-2.rds.amazonaws.com',
            database = 'memo_db',
            user = 'soej',
            password = 'soej1234')
    
    return connection