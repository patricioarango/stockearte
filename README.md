# stockearte
DSSD-Stockearte-Grupo16

## remote db connection
host: mysql-1d36c064-pato-ef11.a.aivencloud.com <br />
port: 25628 <br />
db: stockeartedb <br />
user: avnadmin <br />
password: AVNS_ylqtAU8JPG7TNXz0mDD <br />

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
- id provincia
- habilitado (boolean)

PROVINCIA (db harcodeada en db)
- id provincia
- nombre
  
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
