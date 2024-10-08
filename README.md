# Stockearte
DSSD-Stockearte-Grupo16

## Conexión db remota
https://trello.com/c/6kH1vAE0/11-conexi%C3%B3n-a-base-de-datos-remota

## Estrategia de desarrollo
https://docs.google.com/document/d/1vtV1L3HOr8xi34foe9OASbyZ5cb5SSquEIJoxBqp1YM/edit

## Maqueta inicial de frontend:
https://excalidraw.com/#room=428675ecde542f67de6a,N7tYjxZP9RnOSL-sh6Vvjg


## Ambiente

- Visual Studio Code
- Server Java (JDK 17)
- Cliente Python con Flask
- MySQL

## Inicio Apache Kafka
cd C:\Kafka
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
en otra terminal:
cd C:\Kafka
.\bin\windows\kafka-server-start.bat .\config\server.properties
### Listar todos los topics que existen dentro del broker:
.\bin\windows\kafka-console-consumer.bat --topic orden-de-compra --bootstrap-server localhost:9092

## Inicio proyecto ServerJava

Ingresar los siguientes comandos en la terminal:

1. cd ServidorJava 
2. mvn clean install -DskipTests
3. mvn spring-boot:run

## Inicio ClientePy
4. cd ClientePy 
5. pip install -r requirements.txt
6. python main.py
7. ejecutar inserts.sql en MySQL para tener usuarios creados.
8. acceder a http://localhost:5000/ 

## Inicio Proveedor App
9. cd proveedorPy 
10. pip install -r requirements.txt
11. python main.py
12. ejecutar inserts.sql en MySQL para tener usuarios creados.
13. acceder a http://localhost:5001/ 

## Comandos para la modificación de los stubs de python
   
 python -m grpc_tools.protoc -I../ServidorJava/src/main/proto --python_out=. --pyi_out=. --grpc_python_out=. ../ServidorJava/src/main/proto/user.proto
 python -m grpc_tools.protoc -I../ServidorJava/src/main/proto --python_out=. --pyi_out=. --grpc_python_out=. ../ServidorJava/src/main/proto/product.proto
 python -m grpc_tools.protoc -I../ServidorJava/src/main/proto --python_out=. --pyi_out=. --grpc_python_out=. ../ServidorJava/src/main/proto/productStock.proto
 python -m grpc_tools.protoc -I../ServidorJava/src/main/proto --python_out=. --pyi_out=. --grpc_python_out=. ../ServidorJava/src/main/proto/role.proto
 python -m grpc_tools.protoc -I../ServidorJava/src/main/proto --python_out=. --pyi_out=. --grpc_python_out=. ../ServidorJava/src/main/proto/store.proto
python -m grpc_tools.protoc -I../ServidorJava/src/main/proto --python_out=. --pyi_out=. --grpc_python_out=. ../ServidorJava/src/main/proto/orderItem.proto
python -m grpc_tools.protoc -I../ServidorJava/src/main/proto --python_out=. --pyi_out=. --grpc_python_out=. ../ServidorJava/src/main/proto/purchaseOrder.proto
python -m grpc_tools.protoc -I../ServidorJava/src/main/proto --python_out=. --pyi_out=. --grpc_python_out=. ../ServidorJava/src/main/proto/novelty.proto
python -m grpc_tools.protoc -I../ServidorJava/src/main/proto --python_out=. --pyi_out=. --grpc_python_out=. ../ServidorJava/src/main/proto/dispatchOrder.proto
