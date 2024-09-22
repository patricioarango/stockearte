
DROP SCHEMA IF EXISTS `stockearte` ;
CREATE SCHEMA IF NOT EXISTS `stockearte` DEFAULT CHARACTER SET utf8mb3 ;

USE `stockearte` ;

INSERT INTO stockearte.`role` (`role`,`enabled`)
VALUES
	('admin', 1 ),
	('manager', 1);    
    
INSERT INTO stockearte.`store` (`store`,`address`,`city`, `state`,`code`, `enabled`)
VALUES
	('Adidas Sur','Donovan y General Chamiso 1234', 'Gerli',  'Buenos Aires', '123ABC' , 1),
	('Adidas Patagonia','Av. Siempre Viva 5678', 'Arlen',  'Tierra del fuego', '654ZXY' , 1);    
    
INSERT INTO stockearte.`user` (`username`,`name`, `lastname`,`password`, `enabled`,`id_role`, `id_store`)
VALUES
	('admin','Carlos', 'Archundia',  'admin', 1 , 1, 2),
	('user', 'Cornelio', 'Del Rancho', 'user', 1, 2, 1);
        
   
INSERT INTO product (product, code, color, size, img, enabled) VALUES
('Camiseta Deportiva', 'PROD001', 'Rojo', 'M', 'camiseta_roja.jpg', true),
('Pantalón Jeans', 'PROD002', 'Azul', '32', 'jeans_azules.jpg', true),
('Zapatillas Running', 'PROD003', 'Negro', '42', 'zapatillas_negras.jpg', true);

INSERT INTO product_stock (stock, id_product, id_store) VALUES
(50, 1, 1),
(30, 2, 1),
(20, 3, 2),  
(15, 1, 2),  
(10, 2, 2);  
    