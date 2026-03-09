import mysql.connector
import config 

conexion = mysql.connector.connect(
    host = config.HOST,
    user = config.USER,
    port = config.PORT,
    password = config.PASSWORD,
    database = config.DATABASE
)

def get_connection():
    