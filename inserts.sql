
DROP SCHEMA IF EXISTS `stockearte` ;
CREATE SCHEMA IF NOT EXISTS `stockearte` DEFAULT CHARACTER SET utf8mb3 ;

USE `stockearte` ;

INSERT INTO stockearte.`role` (`role`,`enabled`)
VALUES
	('admin', 1 ),
	('manager', 1);    
    
INSERT INTO stockearte.`store` (`store`,`address`,`city`, `state`,`code`, `enabled`)
VALUES
	('Casa Central','Yrigoyen 1234', 'San Telmo',  'CABA', '222AAA' , 1),
    ('Adidas Sur','Donovan y General Chamiso 1234', 'Gerli',  'Buenos Aires', '123ABC' , 1),
	('Adidas Patagonia','Av. Siempre Viva 5678', 'Arlen',  'Tierra del fuego', '654ZXY' , 1);    
    
INSERT INTO stockearte.`user` (`username`,`name`, `lastname`,`password`, `enabled`,`id_role`, `id_store`)
VALUES
	('admin','Carlos', 'Archundia',  'admin', 1 , 1, 1),
	('user', 'Cornelio', 'Del Rancho', 'user', 1, 2, 2),
    ('manager', 'Armando', 'Barrera', 'manager', 1, 2, 2);
        
   
INSERT INTO product (product, code, color, size, img, enabled) VALUES
('Camiseta Deportiva', 'PROD001', 'Rojo', 'M', 'https://highrunner.com.ar/wp-content/uploads/2023/05/CD054.jpg', true),
('Pantalón Jeans', 'PROD002', 'Azul', '32', 'https://www.grupooxicas.com/3082-thickbox_default/pantalon-jean-far-west-indigo-14-onzas-talles-del-38-al-60.jpg', true),
('Zapatillas Running', 'PROD003', 'Negro', '42', 'https://media2.solodeportes.com.ar/media/catalog/product/cache/7c4f9b393f0b8cb75f2b74fe5e9e52aa/z/a/zapatillas-running-adidas-runfalcon-3-0-negra-90497022-100010hq3790001-1.jpg', true);

INSERT INTO product_stock (stock, id_product, id_store) VALUES
(50, 1, 1),
(30, 2, 1),
(20, 3, 2),  
(15, 1, 2),  
(10, 2, 2);  
    