import sqlite3


# These will be test details until this is hooked up to the other programs
admin_user = "admin"
admin_pass = "pass"

users = [admin_user]


def login():
    valid_login = False

    while not valid_login:
        usernameI = str(input("Please enter your username:\t"))
        if usernameI in users:
            passwordI = str(input("Please enter your password:\t"))
            # TODO: if this password is the password of the user let them through
            valid_login = True
