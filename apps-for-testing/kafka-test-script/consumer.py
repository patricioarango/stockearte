from kafka import KafkaConsumer
import time,os,json
import pymysql
from dotenv import load_dotenv

load_dotenv()
TOPIC_NAME = "novedades"
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_USER = os.getenv("DB_USER")
DB_PORT = int(os.getenv("DB_PORT"))
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
connection = None

def connect_to_mysql():
    global connection
    try:
        connection = pymysql.connect(
            host=DB_HOST,  
            port=DB_PORT,       
            user=DB_USER,
            password=DB_PASSWORD,  
            database=DB_NAME, 
        )
        print("Connected to MySQL database")

    except pymysql.MySQLError as e:
        print(f"Error while connecting to MySQL: {e}")
        connection = None

def close_connection():
    if connection:
        connection.close()
        print("MySQL connection closed")

def procesarOrdenSolicitada(orden_de_compra):
    for item in orden_de_compra.get("items"):
        print(f"Procesando item {item}")

def consumerOrdenDeCompra():
    consumer = KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=f"kafka-871a578-pato-ef11.j.aivencloud.com:25630",
        client_id = "CONSUMER_CLIENT_ID",
        group_id = "CONSUMER_GROUP_PROV2",
        security_protocol="SSL",
        ssl_cafile="ca.pem",
        ssl_certfile="service.cert",
        ssl_keyfile="service.key",
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    while True:
        for message in consumer:
            print("message")
            print(message)
            orden_de_compra = message.value 
            print(f"Message received: {orden_de_compra}")
            status = orden_de_compra.get("estado")
            match status:
                case 'SOLICITADA':
                    procesarOrdenSolicitada(orden_de_compra)

if __name__ == "__main__":
    connect_to_mysql()
    if connection:
        consumerOrdenDeCompra()
        close_connection()                