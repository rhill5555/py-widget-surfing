from mysql.connector import MySQLConnection

class SqlComm:
    @staticmethod
    def append_to_table(mysql_connection: MySQLConnection, table: str, columns: dict):
        mycursor = mysql_connection.cursor()
        mycursor.execute(f"""INSERT INTO '{table}' (continent) VALUES
                             ('{columns.name}', {columns.dataType}); 
                             """)
        result = mycursor.fetchall()

