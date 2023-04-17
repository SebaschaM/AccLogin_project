import time

from config import *
from utils import *
from bcrypt import hashpw, gensalt

user_collection = db['user']


# Register
def register(user):
    user["password"] = hashpw(user["password"].encode(
        "utf-8"), gensalt()).decode("utf-8")
    user["createdAt"] = time.time()
    user_collection.insert_one(user)


# Login
def getUserByEmail(email):
    user = user_collection.find_one({"email": email})
    user = object_as_dict(user)
    return user
