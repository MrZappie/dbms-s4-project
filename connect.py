import mysql.connector

def execute(query):
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sidhu123",
        database="dbmspro",
        use_pure=True
    )

    cursor = con.cursor()
    result = cursor.execute(query)
    con.commit()
    return result
