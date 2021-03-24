import pymysql


class dbController:
    def __init__(self, hostIP, hostPort, hostPass, dbUser, dbName):
    
        #Atributos
        self.host = hostIP
        self.port = hostPort
        self.username = dbUser
        self.db = dbName
        self.password = hostPass

        self.connection = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.username,
            password=self.password,
            db=self.db
        )

        self.cursor = self.connection.cursor()

    #Metodo de instancia
    def getAllUsers(self):
        self.cursor.execute("SELECT * FROM Usuarios")
        rows = self.cursor.fetchall()
        self.dbCloseConnection()
        return rows

    #Problema 1
    def insertNewUser(self, usName, usPass, usEmail, now):
        sql = "INSERT INTO Usuarios (Username, Password, Email, CreationD) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (usName, usPass, usEmail, now))
        self.connection.commit()
        self.dbCloseConnection()

    #Problema 2
    def modificarUser(self, usName, usPass, usEmail, usName2):
        sql = "UPDATE Usuarios SET Username = %s, Password = %s, Email = %s WHERE Username = %s;"
        self.cursor.execute(sql,(usName, usPass, usEmail, usName2))
        self.connection.commit()
        self.dbCloseConnection()

    #Problema 3
    def getUser(self, usName):
        sql = "SELECT * FROM Usuarios WHERE Username = %s"
        self.cursor.execute(sql, usName)
        rows = self.cursor.fetchall()
        self.dbCloseConnection()
        return rows
        print(rows)

    #Problema 4
    def getCompras(self, usName):
        sql = "SELECT Username, TotalCompra, FechaHoraC FROM Usuarios INNER JOIN Compras ON Usuarios.Id = Compras.IDUsuario WHERE Username = %s"
        self.cursor.execute(sql, usName)
        rows = self.cursor.fetchall()
        self.dbCloseConnection()
        return rows

    #Problema 5
    def insertCompras(self, usTotalC, now, userId):
        sql = "INSERT INTO Compras(TotalCompra, FechaHoraC, IDUsuario) VALUES(%s, %s, %s);"
        self.cursor.execute(sql, (usTotalC, now, userId))
        self.connection.commit()
        self.dbCloseConnection()

    #Problema 6
    def comprasFecha(self, fec1, fec2):
        sql = "SELECT * FROM Compras WHERE FechaHoraC Between %s And %s;"
        self.cursor.execute(sql, (fec1, fec2))
        rows = self.cursor.fetchall()
        self.dbCloseConnection()
        return rows

    #Problea 7
    def consultaComprasVTs(self, usTotalC):
        sql = "SELECT * FROM Compras WHERE TotalCompra <= %s;"
        self.cursor.execute(sql, usTotalC)
        rows = self.cursor.fetchall()
        self.dbCloseConnection()
        return rows

    #Problema 8
    def getProduct(self):
        sql = "SELECT Nombre, PrecioU FROM Productos"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        self.dbCloseConnection()
        return rows

    #Problema 9
    def updateMonto(self, usTotalC, compraId):
        sql = "UPDATE Compras SET TotalCompra = %s WHERE Id = %s;"
        self.cursor.execute(sql, (usTotalC, compraId))
        self.connection.commit()
        self.dbCloseConnection()

    #Problema 10
    def updateCantidadPrecio(self, usCantidad, usSubTotal, userId):
        sql = "UPDATE DetalleCompras SET Cantidadc = %s, SubTotal = %s WHERE Id = %s;"
        self.cursor.execute(sql, (usCantidad, usSubTotal, userId))
        self.connection.commit()
        self.dbCloseConnection()

    #Cerrar la coneccion para la bd
    def dbCloseConnection(self):
        self.connection.close()