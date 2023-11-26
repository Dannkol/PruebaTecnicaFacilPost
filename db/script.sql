DROP DATABASE `InvFacilPost`;

CREATE DATABASE IF NOT EXISTS `InvFacilPost`;

USE `InvFacilPost`;

CREATE TABLE IF NOT EXISTS `Productos` (
  `Id` INT AUTO_INCREMENT NOT NULL,
  `Nombre` VARCHAR(255) NOT NULL,  
  `Precio` DOUBLE NOT NULL,
  `Descripcion` LONGTEXT NOT NULL,
  `Ref` VARCHAR(255) NOT NULL,
  `Asset` VARCHAR(255),     

  PRIMARY KEY (`Id`)
);


CREATE TABLE IF NOT EXISTS `Categorias` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `Nombre` VARCHAR(255) NOT NULL,    

  PRIMARY KEY (`Id`)
);

CREATE TABLE IF NOT EXISTS `Imagenes` (
  `Id` INT AUTO_INCREMENT NOT NULL,
  `Img` LONGTEXT NOT NULL,    

  PRIMARY KEY (`Id`)
);

CREATE TABLE IF NOT EXISTS `Imagenes_de_Productos` (
  `Id_Img` INT NOT NULL,
  `Id_Productos` INT NOT NULL,    

  PRIMARY KEY (`Id_Img`, `Id_Productos`),
  FOREIGN KEY (`Id_Img`) REFERENCES `Imagenes` (`Id`) ON DELETE CASCADE,
  FOREIGN KEY (`Id_Productos`) REFERENCES `Productos` (`Id`) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS `Categorias_de_Productos` (
  `Id_Categoria` INT NOT NULL,
  `Id_Productos` INT NOT NULL,    

  PRIMARY KEY (`Id_Categoria`, `Id_Productos`),
  FOREIGN KEY (`Id_Categoria`) REFERENCES `Categorias` (`Id`) ON DELETE CASCADE,
  FOREIGN KEY (`Id_Productos`) REFERENCES `Productos` (`Id`) ON DELETE CASCADE
);


-- Insertar datos en la tabla Productos
INSERT INTO Productos (Nombre, Precio, Descripcion, Ref, Asset) VALUES
('Producto1', 19.99, 'Descripción del Producto 1', 'REF001', NULL),
('Producto2', 29.99, 'Descripción del Producto 2', 'REF002', NULL),
('Producto3', 39.99, 'Descripción del Producto 3', 'REF003', 'models/mesa_simple.glb');


-- Insertar datos en la tabla Categorias
INSERT INTO Categorias (Nombre) VALUES
('Electrónicos'),
('Ropa'),
('Hogar');

-- Insertar datos en la tabla Imagenes
INSERT INTO Imagenes (Img) VALUES
('img/imagen1.jpg'),
('img/imagen2.jpg'),
('img/imagen3.jpg');

-- Insertar datos en la tabla Imagenes_de_Productos
INSERT INTO Imagenes_de_Productos (Id_Img, Id_Productos) VALUES
(1, 1),  
(2, 2),  
(3, 3);  

-- Insertar datos en la tabla Categorias_de_Productos
INSERT INTO Categorias_de_Productos (Id_Categoria, Id_Productos) VALUES
(1, 1),  
(2, 2), 
(3, 3);  
