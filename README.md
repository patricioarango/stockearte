# stockearte
DSSD-Stockearte-Grupo16

## conexión db remota
https://trello.com/c/6kH1vAE0/11-conexi%C3%B3n-a-base-de-datos-remota

## estructura de datos
ROL
- id rol
- rol
  
USUARIO:
- id usuario
- id rol
- nombre 
- contraseña
- nombre
- apellido
- id tienda
- habilitado (boolean)

TIENDA
- id tienda
- código alfanumérico (varchar 255)
- nombre 
- dirección (varchar 255 incluye calle y número)
- ciudad (varchar 255)
-  provincia (varchar 255)
- habilitado (boolean)
 
PRODUDCTO
- id producto
- nombre
- código (varchar 10)
- foto

PRODUCTO STOCK
- id producto
- id talle
- id color
- stock 
