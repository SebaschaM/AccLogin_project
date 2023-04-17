# Aqui van los servicios que interactuan con la BD
import time

from config import *
from utils import *
from bcrypt import hashpw, checkpw, gensalt

user_collection = db['user']


def insertUser(user):
    user["password"] = hashpw(user["password"].encode(
        "utf-8"), gensalt()).decode("utf-8")
    user["createdAt"] = time.time()
    user_collection.insert_one(user)


def getUserByEmail(email, isLogin):
    user = user_collection.find_one({"email": email})
    if user:
        user.pop("fullname")
    user = object_as_dict(user)
    return user
