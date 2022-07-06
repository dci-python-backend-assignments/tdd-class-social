import pickle


class DBException(Exception):
    pass


def save_users(users):
    with open('users.pickle', 'wb') as file:
        pickle.dump(users, file)


def load_users():
    try:
        with open('users.pickle', 'rb') as file:
            users = pickle.load(file)
            return users
    except FileNotFoundError:
        with open('users.pickle', 'wb') as file:
            pickle.dump([], file)
        return []


def load_posts():
    try:
        with open('posts.pickle', 'rb') as file:
            posts = pickle.load(file)
            return posts
    except FileNotFoundError:
        with open('posts.pickle', 'wb') as file:
            pickle.dump([], file)
        return []
