import mysql.connector

def get_connection() :
    connection = mysql.connector.connect(
            host = 'yh.cpos3ccatavx.ap-northeast-2.rds.amazonaws.com',
            database = 'memo_db',
            user = 'memo_user2',
            password = 'memo1234')
    
    return connection