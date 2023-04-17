from flask import session, redirect, url_for
from models import User
from config import *


def register_user(name, email, password):
    # Validar que el correo electrónico no esté registrado previamente
    if User.query.filter_by(email=email).first():
        return False, 'El correo electrónico ya está registrado'

    # Validar que la contraseña tenga al menos 8 caracteres
    if len(password) < 8:
        return False, 'La contraseña debe tener al menos 8 caracteres'

    # Crear un nuevo usuario y guardarlo en la base de datos
    user = User(name=name, email=email, password=password)
    db.session.add(user)
    db.session.commit()

    return True, 'Usuario registrado correctamente'


def login_user(email, password):
    # Buscar al usuario por correo electrónico
    user = User.query.filter_by(email=email).first()

    # Verificar que el usuario existe y que la contraseña es correcta
    if user and user.check_password(password):
        # Crear una sesión de usuario
        session['user_id'] = user.id
        return True, 'Inicio de sesión exitoso'

    return False, 'Correo electrónico o contraseña incorrectos'


def logout_user():
    # Eliminar la sesión de usuario
    session.pop('user_id', None)
    return redirect(url_for('index'))
