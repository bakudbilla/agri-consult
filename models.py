import sqlite3
from config import Config
from werkzeug.security import generate_password_hash, check_password_hash

def init_db():
    conn = sqlite3.connect(Config.DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  first_name TEXT, last_name TEXT, username TEXT UNIQUE, password TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS posts
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  author TEXT, title TEXT, content TEXT, date TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS replies
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  post_id INTEGER, author TEXT, content TEXT, date TEXT,
                  FOREIGN KEY (post_id) REFERENCES posts (id))''')
    conn.commit()
    conn.close()

    
class User:
    def __init__(self, id, username, password, is_active=True):
        self.id = id
        self.username = username
        self.password = password
        self._is_active = is_active  # Private attribute to store the active status

    def get_id(self):
        return str(self.id)

    @staticmethod
    def hash_password(password):
        return generate_password_hash(password)

    @staticmethod
    def verify_password(password, hashed_password):
        return check_password_hash(hashed_password, password)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, value):
        if isinstance(value, bool):
            self._is_active = value
        else:
            raise ValueError("is_active must be a boolean value")

    @property
    def is_anonymous(self):
        return False
