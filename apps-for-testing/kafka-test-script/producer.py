import time,os,json
from kafka import KafkaProducer
import pymysql
from dotenv import load_dotenv

load_dotenv()

TOPIC_NAME = "orden_de_compra"

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

def queryODC():
    with connection.cursor() as cursor:
        query = "SELECT * FROM orden_de_compra odc WHERE estado='SOLICITADA' LIMIT 5;"
        cursor.execute(query)
        result = cursor.fetchall()
        return result

def close_connection():
    if connection:
        connection.close()
        print("MySQL connection closed")

def produceOrdenDeCompra():
    print(f"produciendo mensajes kafka")
    producer = KafkaProducer(
        bootstrap_servers=f"kafka-871a578-pato-ef11.j.aivencloud.com:25630",
        security_protocol="SSL",
        ssl_cafile="ca.pem",
        ssl_certfile="service.cert",
        ssl_keyfile="service.key",
        value_serializer=lambda v: json.dumps(v).encode('utf-8') 
    )
    
    for i in range(100):
        results = queryODC()
        for result in results:
            message_dict = {
            "id": result[0],  # Assuming the first element is the ID
            "estado": result[1],  # Assuming the second element is the estado
            "fecha_creacion": str(result[2]),  # Assuming datetime, convert to string
            "fecha_actualizacion": str(result[3]),  # Assuming datetime, convert to string
            }
            message = f"Orden de compra {result}"
            producer.send(TOPIC_NAME,message_dict)
            print(f"Message sent: {message}")
            time.sleep(10)

    producer.close()

if __name__ == "__main__":
    connect_to_mysql()
    if connection:
        produceOrdenDeCompra()
        close_connection()