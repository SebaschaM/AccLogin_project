from config import *
from bcrypt import checkpw
import services


def register(name, email, password):
    user = services.getUserByEmail(email)

    if user:
        return {'message': 'El correo electrónico ya está registrado', 'hasError': True}

    services.register({
        'name': name,
        'email': email,
        'password': password
    })
    return {'message': 'Usuario registrado correctamente', 'hasError': False}


def login(email, password):
    user = services.getUserByEmail(email)

    if not user:
        return {'message': 'Correo electrónico o contraseña incorrectos', 'hasError': True}

    if not checkpw(password.encode("utf-8"), user['password'].encode("utf-8")):
        return {'message': 'Correo electrónico o contraseña incorrectos', 'hasError': True}

    return {'message': 'Bienvenido', 'hasError': False}
