import psycopg2

database="login",
user="postgres",
password="Agnavinod_kjc123",
host="localhost"
port=5432

conn = psycopg2.connect(
    dbname=database,
    user=user,
    password=password,
    host=host,
    port=port)
    
conn.close()