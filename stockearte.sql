-- Schema stockearte
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `stockearte` ;

-- -----------------------------------------------------
-- Schema stockearte
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `stockearte` DEFAULT CHARACTER SET utf8mb3 ;
USE `stockearte` ;

CREATE TABLE `rol` (
  `id_rol` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `rol` VARCHAR(255) DEFAULT NULL,
  `enabled` BOOLEAN DEFAULT TRUE,
  PRIMARY KEY (`id_rol`)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE `store` (
  `id_store` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `store` VARCHAR(255) DEFAULT NULL,
  `code` VARCHAR(255) DEFAULT NULL,
  `address` VARCHAR(255) DEFAULT NULL,
  `city` VARCHAR(255) DEFAULT NULL,
  `state` VARCHAR(255) DEFAULT NULL,
  `enabled` BOOLEAN DEFAULT TRUE,
  PRIMARY KEY (`id_store`)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE `user` (
  `id_user` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(255) DEFAULT NULL,
  `name` VARCHAR(255) DEFAULT NULL,
  `lastname` VARCHAR(255) DEFAULT NULL,
  `password` VARCHAR(255) DEFAULT NULL,
  `enabled` BOOLEAN DEFAULT TRUE,
  `id_rol` INT(11) UNSIGNED DEFAULT NULL,
  `id_store` INT(11) UNSIGNED DEFAULT NULL,
  PRIMARY KEY (`id_user`),
  FOREIGN KEY (`id_rol`) REFERENCES `rol` (`id_rol`),
  FOREIGN KEY (`id_store`) REFERENCES `store` (`id_store`)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE `product` (
  `id_product` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `product` VARCHAR(255) DEFAULT NULL,
  `code` VARCHAR(10) DEFAULT NULL,
  `img` VARCHAR(255) DEFAULT NULL,
  `enabled` BOOLEAN DEFAULT TRUE,
  `size` VARCHAR(255) DEFAULT NULL,
  `color` VARCHAR(255) DEFAULT NULL,
  PRIMARY KEY (`id_product`)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE `product_stock` (
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `id_product` INT(11) UNSIGNED NOT NULL,
  `id_store` INT(11) UNSIGNED NOT NULL,
  `stock` INT(11) DEFAULT 0,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`id_product`) REFERENCES `product` (`id_product`),
  FOREIGN KEY (`id_store`) REFERENCES `store` (`id_store`)
) ENGINE=INNODB DEFAULT CHARSET=utf8;


CREATE TABLE `purchase_order` (
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `observation` TEXT DEFAULT NULL,
  `id_store` int DEFAULT NULL,
  `state`  ENUM('RECHAZADA','ACEPTADA','SOLICITADA','RECIBIDA') DEFAULT 'SOLICITADA',
  `created_at` DATETIME DEFAULT NULL,
  `purchase_order_date` DATETIME DEFAULT NULL,
  `reception_date` DATETIME DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE `order_item` (
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `id_purchase_order` int NOT NULL,
  `product_code` varchar(255) DEFAULT NULL,
  `color` varchar(255) DEFAULT NULL,
  `size` varchar(255) DEFAULT NULL,
  `requested_amount` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8;
