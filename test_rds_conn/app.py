import psycopg2

def establish_connection():
    
    db_host = 'test-instance.cbwqge2ke8p3.ap-southeast-1.rds.amazonaws.com'
    db_port = 5432
    db_name = 'testdb'
    db_username = 'postgres'
    db_password = 'Albino123'
    
    try:
        connection = psycopg2.connect(database=db_name,
                                      user=db_username,
                                      password=db_password,
                                      host=db_host,
                                      port=db_port)
        return connection
    except Exception as e:
        raise Exception(f"Connection failed: {str(e)}")

def lambda_handler(event, context):
    
    connection = establish_connection()
    if connection:
        connection.close()
        return {
            'statusCode': 200,
            'body': 'Connection Established Successfully'
        }