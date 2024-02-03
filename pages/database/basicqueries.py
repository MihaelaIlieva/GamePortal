import sqlite3

def add_user(username, password):
    connection = sqlite3.connect('database/game_portal.db')
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO users(username, password) VALUES (?,?)''',(username,password))
    connection.commit()
    connection.close()

def check_for_same_username(username):
    connection = sqlite3.connect('database/game_portal.db')
    cursor = connection.cursor()
    cursor.execute('''SELECT id from users WHERE username=?''',(username,))
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result

def get_user_credentials(id):
    connection = sqlite3.connect('database/game_portal.db')
    cursor = connection.cursor()
    cursor.execute('''SELECT username, password from users WHERE id=?''',(id,))
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result

def get_all_users():
    connection = sqlite3.connect('database/game_portal.db')
    cursor = connection.cursor()
    cursor.execute('''SELECT * from users''')
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result