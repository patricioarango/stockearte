# Stockearte
DSSD-Stockearte-Grupo16

## Conexión db remota
https://trello.com/c/6kH1vAE0/11-conexi%C3%B3n-a-base-de-datos-remota

## Estrategia de desarrollo GRPC
https://docs.google.com/document/d/1vtV1L3HOr8xi34foe9OASbyZ5cb5SSquEIJoxBqp1YM/edit

## Maqueta inicial de frontend GRPC:
https://excalidraw.com/#room=428675ecde542f67de6a,N7tYjxZP9RnOSL-sh6Vvjg

## Estrategia de desarrollo Kafka
https://docs.google.com/document/d/e/2PACX-1vRSbuvCN5qZc2lvL4Et7pj8By-ZfR61shJFlSaC3YoRgJqn2YrHrYVaU8WU2HKXSYljHhK-w4IBfL-r/pub

## Diagrama Kafka:
https://excalidraw.com/#json=AaTG1XGfNlNHoFIDMhfdH,dPwy_5mtEXqTs7rMdMOr_A

## Ambiente
- Visual Studio Code
- Server Java (JDK 17)
- Cliente Python con Flask
- MySQL

# Inicio proyecto ServerJavaSoap
Ingresar los siguientes comandos en la terminal:
1. cd ServerJavaSoap 
2. mvn clean install -DskipTests
3. mvn spring-boot:run

## Inicio SoapClient
4. cd SoapClient 
5. pip install -r requirements.txt
6. python main.py

## Inicio Rest-app
7. cd rest-app 
8. pip install -r requirements.txt
9. python main.py


# Inicio proyecto ServerJava (GRPC + Kafka)
Ingresar los siguientes comandos en la terminal:
1. cd ServidorJava 
2. mvn clean install -DskipTests
3. mvn spring-boot:run

## Inicio Apache Kafka
3. cd C:\Kafka
4. .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties

En otra terminal:

5. cd C:\Kafka
6. .\bin\windows\kafka-server-start.bat .\config\server.properties
### Listar todos los topics que existen dentro del broker:
.\bin\windows\kafka-console-consumer.bat --topic orden-de-compra --bootstrap-server localhost:9092

## Inicio ClientePy
7. cd ClientePy 
8. pip install -r requirements.txt
9. python main.py
10. ejecutar inserts.sql en MySQL para tener usuarios creados.
11. acceder a http://localhost:5000/ 

## Inicio ProveedorPy
12. cd proveedorPy 
13. pip install -r requirements.txt
14. python main.py
15. acceder a http://localhost:5001/ 

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


## Soap Server JAVA - WSDLs
SOAP_WSDL_CATALOGOS='http://localhost:8080/wsc/catalogos.wsdl'
SOAP_WSDL_USUARIOS='http://localhost:8080/wsu/users.wsdl'
SOAP_WSDL_INFORMES='http://localhost:8080/wsi/informes.wsdl'
SOAP_WSDL_PRODUCTOS='http://localhost:8080/wsp/productos.wsdl'
SOAP_WSDL_TIENDAS='http://localhost:8080/wst/tiendas.wsdl'