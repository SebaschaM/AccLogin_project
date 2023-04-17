# Aqui va la configuracion para la conexion a la BD
import pymongo


MONGO_URI = "mongodb+srv://schaquila:sebas123@cluster0.saeuaek.mongodb.net/?retryWrites=true&w=majority"
DB_NAME = "Accounts"

client = pymongo.MongoClient(MONGO_URI)
db = client[DB_NAME]
user_collection = db['user']
