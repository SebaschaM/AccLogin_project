# Aqui van los modelos las cuales representan los datos en la BD
from bson import schema

user_schema = schema.Schema({
    '_id': schema.Optional(schema.ObjectId),
    'nombre': schema.And(str, lambda x: 3 <= len(x) <= 50),
    'correo': schema.And(str, lambda x: '@' in x),
    'password': schema.And(str, lambda x: len(x) >= 6)
})
