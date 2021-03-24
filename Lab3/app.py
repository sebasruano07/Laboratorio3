from flask import Flask, request, jsonify
import json
import collections
import hashlib
from datetime import datetime

import DBController as DBC 

app = Flask(__name__)

#Nuevo Usuario
@app.route('/newUser', methods=['POST'])
def create_new_user():
    try:
        data = request.get_json()
        dbConnection = DBC.dbController('127.0.0.1', 3306, 'SebastianR1', 'root', 'Lab1')

        #Encripcion del password
        usPass = hashlib.md5(data['Password'].encode('utf-8'))
        usNameEncode = hashlib.md5(data['Username'].encode('utf-8'))
        usPassEncode = (usNameEncode.hexdigest() + usPass.hexdigest()).encode('utf-8')
        encriptedPass = (hashlib.md5(usPassEncode).hexdigest())
        elMail = (data['Email'])

        #insertamos fecha
        now = datetime.now().strftime("%Y-%m-%d")
        print(now)
        print(elMail)

        dbConnection.insertNewUser(data['Username'], encriptedPass, elMail, now)
        return jsonify({'mensssage': 'Usuario creado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensssage': 'Ocurrio un error'})

#Consulta de usuario
@app.route('/consulta/<usName>', methods=['GET'])
def get_user_(usName):
    try:
        data = request.get_json()
        dbConnection = DBC.dbController('127.0.0.1', 3306, 'SebastianR1', 'root', 'Lab1')
        salida = dbConnection.getUser(usName)
        return jsonify(salida)

        print(salida)

    except Exception as ex:
        print(ex)
        return jsonify({'message': 'Ocurrio un problema'})

#Consulta de todos los porductos
@app.route('/productos', methods=['GET'])
def get_Product_():
    try:
        data = request.get_json()
        dbConnection = DBC.dbController('127.0.0.1', 3306, 'SebastianR1', 'root', 'Lab1')
        producto = dbConnection.getProduct()
        return jsonify(producto)
        
    except Exception as ex:
        print(ex)
        return jsonify({'message': 'Ocurrio un problema'})

#Editar la cantidad y precio del detalle de compra
@app.route('/EcantidadPrecio/<userId>', methods=['PUT'])
def get_Product(userId):
    try:
        data = request.get_json()
        dbConnection = DBC.dbController('127.0.0.1', 3306, 'SebastianR1', 'root', 'Lab1')
        cantidad = data['cantidadc']
        subTotal = data['SubTotal']

        print(cantidad)
        print(subTotal)
        dbConnection.updateCantidadPrecio(cantidad, subTotal, userId)

        return jsonify({'message': 'Cantidad y precio del detalle de compra actualizado.'})

    except Exception as ex:
        print(ex)
        return jsonify({'message': 'Ocurrio un problema'})

#Editar el monto total de una compra
@app.route('/EmontoT/<compraId>', methods=['PUT'])
def get_monto(compraId):
    try:
        data = request.get_json()
        dbConnection = DBC.dbController('127.0.0.1', 3306, 'SebastianR1', 'root', 'Lab1')
        montoTotal = data['TotalCompra']

        print(montoTotal)
        dbConnection.updateMonto(montoTotal, compraId)

        return jsonify({'message': 'El monto total de la compra ha sido actualizado.'})

    except Exception as ex:
        print(ex)
        return jsonify({'message': 'Ocurrio un problema'})

#Insertar una nueva compra
@app.route('/newCompra', methods=['POST'])
def create_new_compra():
    try:
        data = request.get_json()
        dbConnection = DBC.dbController('127.0.0.1', 3306, 'SebastianR1', 'root', 'Lab1')
        Total = data['TotalCompra']
        idUsuario = data['IDUsuario']

        #insertamos fecha
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(now)
        print(Total)
        print(idUsuario)

        dbConnection.insertCompras(Total, now, idUsuario)

        return jsonify({'message': 'Compra creada con exito.'})

    except Exception as ex:
        print(ex)
        return jsonify({'message': 'Ocurrio un problema'})

#Consultar las compras de un usuario
@app.route('/cCompras/<usName>', methods=['GET'])
def get_Compras(usName):
    try:
        dbConnection = DBC.dbController('127.0.0.1', 3306, 'SebastianR1', 'root', 'Lab1')
        lasCompras = dbConnection.getCompras(usName)
        return jsonify(lasCompras)

    except Exception as ex:
        print(ex)
        return jsonify({'message': 'Ocurrio un problema'})

#Consultar montos con rango establecido
@app.route('/consultaVT/<usTotalC>', methods=['GET'])
def get_montos(usTotalC):
    try:
        dbConnection = DBC.dbController('127.0.0.1', 3306, 'SebastianR1', 'root', 'Lab1')
        salida = dbConnection.consultaComprasVTs(usTotalC)
        return jsonify(salida)

    except Exception as ex:
        print(ex)
        return jsonify({'message': 'Ocurrio un problema'})

#Consultar compras que se encuentren en un rango de fechas
@app.route('/ConsultaF', methods=['POST'])
def get_MontosCF1():
    try:
        data = request.get_json()
        dbConnection = DBC.dbController('127.0.0.1', 3306, 'SebastianR1', 'root', 'Lab1')
        fecha1 = data['FechaInicial']
        fecha2 = data['FechaFinal']
        print(fecha1)
        print(fecha2)
        salida = dbConnection.comprasFecha(fecha1, fecha2)
        return jsonify(salida)

    except Exception as ex:
        print(ex)
        return jsonify({'message': 'Ocurrio un problema'})

#Cambiar los datos de usuario
@app.route('/CambiarUser/<user>', methods=['POST'])
def get_cambiarUser(user):
    try:
        data = request.get_json()
        dbConnection = DBC.dbController('127.0.0.1', 3306, 'SebastianR1', 'root', 'Lab1')
        
        #Encripcion del password
        usPass = hashlib.md5(data['Password'].encode('utf-8'))
        usNameEncode = hashlib.md5(data['Username'].encode('utf-8'))
        usPassEncode = (usNameEncode.hexdigest() + usPass.hexdigest()).encode('utf-8')
        encriptedPass = (hashlib.md5(usPassEncode).hexdigest())
        elMail = (data['Email'])

        dbConnection.modificarUser(data['Username'], encriptedPass, elMail, user)
        return jsonify({'message': 'Datos actualizados del usuario con exito.'})

    except Exception as ex:
        print(ex)
        return jsonify({'message': 'Ocurrio un problema'})