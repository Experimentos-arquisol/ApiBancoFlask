from models import Cliente, db

def create_cliente(data):
    try:
        nuevo_cliente = Cliente(
            nombre=data['nombre'],
            apellido=data['apellido'],
            usuario=data['usuario'],
            correo=data['correo'],
            telefono=data['telefono']
        )
        db.session.add(nuevo_cliente)
        db.session.commit()
        return nuevo_cliente
    except Exception as e:
        db.session.rollback()
        print(f"Error al crear el cliente: {e}")
        return None


def buscar_cliente(correo_usuario):
    try:
        cliente = Cliente.query.filter_by(correo=correo_usuario).first()
        if cliente:
            return {'existe': True, 'telefono': cliente.telefono, 'correo':cliente.correo}
        else:
            return None
    except Exception as e:
        print(f"Error al buscar el cliente: {e}")
        return None
    
def get_all_clientes():
    try:
        clientes = Cliente.query.all()
        clientes_list = [{
            'nombre': cliente.nombre,
            'apellido': cliente.apellido,
            'usuario': cliente.usuario,
            'correo': cliente.correo,
            'telefono': cliente.telefono
        } for cliente in clientes]
        return clientes_list
    except Exception as e:
        print(f"Error al obtener los clientes: {e}")
        return None