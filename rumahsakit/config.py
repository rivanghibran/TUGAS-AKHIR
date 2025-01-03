#code by rivanghibran https://github.com/rivanghibran
import psycopg2

def connect_db():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="rumahsakit",
            user="postgres",
            password="admin",
        )
        return conn
    except Exception as e:
        print(f"Error: {e}")
        return None
#code by rivanghibran https://github.com/rivanghibran