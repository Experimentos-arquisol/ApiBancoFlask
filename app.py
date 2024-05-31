import logging
import cliente_logic as cl  
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from models import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'django-insecure-)h&hw17vn5r^pmj$2&$rd!*^q*384iop)lft9xs^_l!6%_oy7^'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://admin_user:sprint321@localhost:5432/usuarios_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)

logging.basicConfig(level=logging.DEBUG)

@app.route('/validar_cliente/', methods=['POST', 'GET'])
@csrf.exempt
def validar_cliente():
    correo_usuario = request.form.get('correo')
    app.logger.debug("Peticion recibida")
    if not correo_usuario:
        return jsonify({"error": "Falta el correo o usuario en la solicitud"}), 400

    resultado = cl.buscar_cliente(correo_usuario)
    if resultado:
        return jsonify({"existe": True, "telefono": resultado['telefono'], 'correo': resultado['correo']}), 200
    else:
        return jsonify({"existe": False}), 404

@app.route('/crear_cliente/', methods=['POST'])
@csrf.exempt
def crear_cliente():
    if request.method == 'POST':
        data = request.form  # Los datos del cliente enviados en la petición
        app.logger.debug("Datos recibidos: %s", data)
        
        if not data:
            return jsonify({"error": "No se recibieron datos"}), 400
        
        resultado = cl.create_cliente(data)
        if resultado:
            return jsonify({"message": "Cliente creado exitosamente"}), 201
        else:
            return jsonify({"error": "No se pudo crear el cliente"}), 400
    return jsonify({"hola": "holaaaa"}), 200
        
@app.route('/prueba/', methods=['GET'])
def prueba():
    return jsonify({"rta": "Holaaa"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

