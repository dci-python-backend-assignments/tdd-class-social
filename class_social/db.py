import pickle
import pymongo

class DBException(Exception):
    pass

client = pymongo.MongoClient("localhost", 27018)
db = client.class_social

def save_users(users):
    with open('users.pickle', 'wb') as file:
        pickle.dump(users, file)


def load_users():
    return db.users.find()
