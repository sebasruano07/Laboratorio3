CREATE DATABASE Lab1;

USE Lab1;

#Tabla de Usuarios
CREATE TABLE Usuarios(
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Username VARCHAR(50) NOT NULL,
    Password VARCHAR(50) NOT NULL,
    Email VARCHAR(60) NOT NULL,
    CreationD DATE NOT NULL
);

#Datos en Usuarios
INSERT INTO Usuarios(Username, Password, Email, CreationD)
    VALUES('Pepe', md5(md5('Pepe') + md5('Contra')), 'pepepalote@gmail.com', NOW());

INSERT INTO Usuarios(Username, Password, Email, CreationD)
    VALUES('Hector', md5(md5('Hector') + md5('ElHector')), 'papalotio@gmail.com', NOW());

#Select de Usuarios
SELECT * FROM Usuarios;

#Tabla de Compras
CREATE TABLE Compras(
    Id INT AUTO_INCREMENT PRIMARY KEY,
    TotalCompra DOUBLE(7,2) NOT NULL,
    FechaHoraC DATETIME NOT NULL,

    IDUsuario INT NOT NULL,

    CONSTRAINT fk_IdUsuario FOREIGN KEY (IDUsuario)
        REFERENCES Usuarios(Id)
        ON DELETE NO ACTION
        ON UPDATE CASCADE
);

#Datos en Compras
INSERT INTO Compras(TotalCompra, FechaHoraC, IDUsuario)
    VALUES(600.00, NOW(), 2);

INSERT INTO Compras(TotalCompra, FechaHoraC, IDUsuario)
    VALUES(50.50, NOW(), 1);

#Select de Compras
SELECT  * FROM Compras;

UPDATE Compras SET TotalCompra = 5000.00 WHERE Id = 2;

#Tabla de Producto
CREATE TABLE Productos(
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(70) NOT NULL,
    Descripcion VARCHAR(100),
    Categoria ENUM('Tecnologia', 'Linea Blanca', 'Moda', 'Cuidado Personal', 'Transporte') NOT NULL,
    PrecioU DOUBLE(6,2) NOT NULL
);

#Datos para Productos
INSERT INTO Productos(Nombre, Descripcion, Categoria, PrecioU)
    VALUES('Rasuradora', 'Esta buenisima', 4, 12.00);

INSERT INTO Productos(Nombre, Descripcion, Categoria, PrecioU)
    VALUES('TV', 'Más o menos', 1, 5000.00);

#Select de Productos
SELECT * FROM Productos;

SELECT Nombre, PrecioU FROM Productos;

#Tabla de Detalle Compras
CREATE TABLE DetalleCompras(
    Id INT AUTO_INCREMENT PRIMARY KEY,
    CantidadC INT NOT NULL,
    SubTotal DOUBLE(8,2) NOT NULL,

    IDCompra INT NOT NULL,
    IDProducto INT NOT NULL,

    CONSTRAINT fk_IdCompra FOREIGN KEY (IDCompra)
        REFERENCES Compras(Id)
        ON DELETE NO ACTION
        ON UPDATE CASCADE,
    CONSTRAINT fk_IdProducto FOREIGN KEY (IDProducto)
        REFERENCES Productos(Id)
        ON DELETE NO ACTION
        ON UPDATE CASCADE
);

#Datos para Detalle Compras
INSERT INTO DetalleCompras(cantidadc, SubTotal, idcompra, idproducto)
    VALUES(2, 24.00, 1, 1);

INSERT INTO DetalleCompras(cantidadc, SubTotal, idcompra, idproducto)
    VALUES(4, 20000.00, 2, 2);

#Select de Detalle Compras
SELECT * FROM DetalleCompras;


SELECT Username, TotalCompra, FechaHoraC FROM Usuarios
INNER JOIN Compras ON Usuarios.Id = Compras.IDUsuario
WHERE Username = 'Hector';
