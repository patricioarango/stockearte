CREATE TABLE "producto" (
  "id" int NOT NULL AUTO_INCREMENT,
  "codigo_producto" varchar(255) DEFAULT NULL,
  PRIMARY KEY ("id")
)

CREATE TABLE "articulo" (
  "id" int NOT NULL AUTO_INCREMENT,
  "id_producto" int DEFAULT NULL,
  "articulo" varchar(255) DEFAULT NULL,
  "id_talle" int DEFAULT NULL,
  "id_color" int DEFAULT NULL,
  "stock" int DEFAULT NULL,
  PRIMARY KEY ("id")
)

CREATE TABLE "color" (
  "id" int NOT NULL AUTO_INCREMENT,
  "color" varchar(255) DEFAULT NULL,
  PRIMARY KEY ("id")
)

CREATE TABLE "talle" (
  "id" int NOT NULL AUTO_INCREMENT,
  "talle" varchar(255) DEFAULT NULL,
  PRIMARY KEY ("id")
)

insert into talle (talle) values ('chico');
insert into talle (talle) values ('mediano');
insert into talle (talle) values ('grande');

insert into color (color) values ('azul');
insert into color (color) values ('rojo');
insert into color (color) values ('negro');
insert into color (color) values ('verde');