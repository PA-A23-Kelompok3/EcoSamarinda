import mysql.connector

def connect_database():
    try:
        mydb = mysql.connector.connect (
            host = "localhost",
            user = "root",
            password = "",
            database = "ecosamarinda"
        )
        cursor = mydb.cursor()
        return mydb, cursor
    except mysql.connector.Error as err:
        print(F"Error: {err}")
        return None, None