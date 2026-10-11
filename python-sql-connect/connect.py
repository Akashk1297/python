import mysql.connector

try:
    # 1. Establish the connection to the database
    connection = mysql.connector.connect(
        host="localhost",        # Replace with your host (e.g., cloud IP or localhost)
        user="***",             # Replace with your MySQL username
        password="***", # Replace with your MySQL password
        database="student" # Replace with your database name
    )
    
    if connection.is_connected():
        print("Successfully connected to the database!")
        
        # 2. Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        
        # 3. Execute a query
        cursor.execute("use student;")
        cursor.execute("show tables;")
        record = cursor.fetchone()
        print("You are connected to database:", record)
        
except mysql.connector.Error as error:
    print(f"Error while connecting to MySQL: {error}")

finally:
    # 4. Always close the cursor and connection when done
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")
