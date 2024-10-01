este es el comando para generar los proto en Python
hay que cambiar la ruta y el nombre del archivo

python3 -m grpc_tools.protoc -I=/home/patricio/Documents/unla/DSSD-Grupo16/SpringBootServer/src/main/proto/ --python_out=. --grpc_python_out=. user.proto