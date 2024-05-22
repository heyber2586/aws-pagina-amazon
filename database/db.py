import pymysql

db_host = 'db-pruebas.cluiwocssnet.us-east-1.rds.amazonaws.com'
db_user = 'heyber'
db_passw = 'heyber25'
db_name = 'db_users'

def connectionSQL():
    try:
        connection = pymysql.connect(
            host = db_host,
            user = db_user,
            password = db_passw,
            database = db_name
            )
        print("Succesfull connection to DB")
        return connection
    except Exception as err:
        print("Error connecting to DB", err)
        return None
        
        
def insert_records(id,name,lastname,birthday):
    query = "INSERT INTO  users (id , name, lastname, birthday ) VALUE ("+id+" ,'"+name+"','"+lastname+"','"+birthday+"')"
    try:
        connection = connectionSQL()
        if connection != None:
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            print("Users added")
        else:
            print("Error in the connection")
        
    except Exception as err:
        print("Error creating the user", err)

def consult_records(id):
    query = "SELECT * FROM users WHERE id = " + id
    try:
        connection = connectionSQL()
        cursor = connection.cursor()
        if connection != None:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        else:
            print("Error creating the user")
            return None
    except Exception as err:
        print("Error consulting the user", err)
        return None