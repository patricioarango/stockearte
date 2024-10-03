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


CREATE TABLE `orden_de_compra` (
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `observaciones` TEXT DEFAULT NULL,
  `id_store` int DEFAULT NULL,
  `estado`  ENUM('RECHAZADA','ACEPTADA','SOLICITADA','RECIBIDA') DEFAULT 'SOLICITADA',
  `fecha_creacion` DATETIME DEFAULT NULL,
  `fecha` DATETIME DEFAULT NULL,
  `fecha_recepcion` DATETIME DEFAULT NULL,
  `id_despacho` int DEFAULT NULL,
   `procesado` int DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE `orden_de_compra_item` (
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `id_orden_de_compra` int NOT NULL,
  `codigo_producto` varchar(255) DEFAULT NULL,
  `color` varchar(255) DEFAULT NULL,
  `size` varchar(255) DEFAULT NULL,
  `cantidad_solicitada` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8; 

CREATE TABLE `despacho` (
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `id_orden_de_pago` int NOT NULL,
  `fecha_estimada_envio` DATETIME DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8; 

insert into talle (talle) values ('chico');
insert into talle (talle) values ('mediano');
insert into talle (talle) values ('grande');

insert into color (color) values ('azul');
insert into color (color) values ('rojo');
insert into color (color) values ('negro');
insert into color (color) values ('verde');
