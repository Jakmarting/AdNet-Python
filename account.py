import sqlite3
import bcrypt

class account:
    def __init__(self, username="", password="pass"):
        self.username = username
        self.password = password

        self.connection = sqlite3.connect('accounts.db')
        self.cursor = self.connection.cursor()

    def load_user(self, username):
        self.cursor.execute("""
        SELECT * FROM accounts
        WHERE username = {}
        """.format(username))

        results = cursor.fetchone()

        self.username = results[0]
        self.password = results[1]

    def insert_user(self):
        
        self.cursor.execute("""
        INSERT INTO accounts VALUES
        ({}, '{}', '{}')
        """.format(self.user_id, self.username, self.password))

        self.connection.commit()
        self.connection.close()
        
u1 = account("FirstUser","ComplexPassword")
u1.insert_user()

connection = sqlite3.connect('accounts.db')
cursor = connection.cursor()
     
cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (,
    username TEXT PRIMARY KEY,
    hashed_password BLOB,
    salt BLOB
)
""")

cursor.execute("SELECT * FROM accounts")
results = cursor.fetchall()
print(results)

connection.commit() # update changes to database
connection.close()
