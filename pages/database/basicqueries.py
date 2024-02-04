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

def add_new_question(question, correct_answer, second_option, third_option, fourth_option, difficulty):
    connection = sqlite3.connect('database/game_portal.db')
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO questions(question, correct_answer, second_option, third_option, fourth_option, difficulty) VALUES (?, ?, ?, ?, ?, ?)''', (question, correct_answer, second_option, third_option, fourth_option, difficulty))
    connection.commit()
    connection.close()

def get_questions_by_difficulty(difficulty):
    connection = sqlite3.connect('database/game_portal.db')
    cursor = connection.cursor()
    cursor.execute('''SELECT * from questions WHERE difficulty=?''',(difficulty,))
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result

def get_correct_answer(question):
    connection = sqlite3.connect('database/game_portal.db')
    cursor = connection.cursor()
    cursor.execute('''SELECT correct_answer from questions WHERE question=?''',(question,))
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result