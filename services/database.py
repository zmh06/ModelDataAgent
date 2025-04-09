# services/database.py
import mysql.connector

def connect():
    try:
        connection = mysql.connector.connect(
            host="192.168.0.102",
            port=3306,
            user="root",
            password="123456",
            database="myagent_info"
        )
        return connection
    except Exception as e:
        print(f"连接失败: {str(e)}")
        return None

def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"执行失败: {str(e)}")
        return None

def get_table_schemas(connection):
    cursor = connection.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    schema_info = ""
    for table in tables:
        table_name = table[0]
        cursor.execute(f"DESCRIBE {table_name}")
        schema = cursor.fetchall()
        schema_info += f"表名: {table_name}\n"
        schema_info += "\n".join([f"- {col[0]} ({col[1]})" for col in schema]) + "\n\n"
    return schema_info