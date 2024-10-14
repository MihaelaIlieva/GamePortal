import sqlite3
DATABASE_PATH = 'database/game_portal.db'

def add_user(username, password):
    
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO users(username, password) VALUES (?,?)''',(username,password))
    connection.commit()
    connection.close()

def check_for_same_username(username):
    
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute('''SELECT id from users WHERE username=?''',(username,))
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result

def get_user_credentials(id):
    
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute('''SELECT username, password from users WHERE id=?''',(id,))
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result

def get_all_users():
    
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute('''SELECT * from users''')
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result

def add_new_question(question, correct_answer, second_option, third_option, fourth_option, difficulty):
    
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO questions(question, correct_answer, second_option, third_option, fourth_option, difficulty) VALUES (?, ?, ?, ?, ?, ?)''', (question, correct_answer, second_option, third_option, fourth_option, difficulty))
    connection.commit()
    connection.close()

def get_questions_by_difficulty(difficulty):
    
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute('''SELECT * from questions WHERE difficulty=?''',(difficulty,))
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result

def get_correct_answer(question):
    
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute('''SELECT correct_answer from questions WHERE question=?''',(question,))
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result

def add_played_game(username, game_name, date_played, questions_answered, outcome):
    
    user_id = check_for_same_username(username)[0][0]
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    if game_name == "become_rich":
        cursor.execute('''INSERT INTO games(user_id, game_name, date_played, guessed_questions) VALUES (?, ?, ?, ?)''', (user_id, game_name, date_played, questions_answered))
    else:
        if outcome == "win":
            cursor.execute('''INSERT INTO games(user_id, game_name, date_played, win) VALUES (?, ?, ?, ?)''', (user_id, game_name, date_played, 1))
        elif outcome == "draw":
            cursor.execute('''INSERT INTO games(user_id, game_name, date_played, draw) VALUES (?, ?, ?, ?)''', (user_id, game_name, date_played, 1))
        elif outcome == "loss":
            cursor.execute('''INSERT INTO games(user_id, game_name, date_played, loss) VALUES (?, ?, ?, ?)''', (user_id, game_name, date_played, 1))
        else:
            pass
    connection.commit()
    connection.close()

def get_high_score_questions(username):
    
    user_id = check_for_same_username(username)[0][0]
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute('''SELECT MAX(guessed_questions) from games WHERE user_id=? AND guessed_questions IS NOT NULL''',(user_id,))
    high_score_questions = cursor.fetchone()[0]
    if high_score_questions == None:
        high_score_questions = 0
    connection.commit()
    connection.close()
    return high_score_questions

def get_date_of_high_score_questions(username, high_score_questions):
    
    user_id = check_for_same_username(username)[0][0]
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute('''SELECT MIN(date_played) from games WHERE user_id=? AND guessed_questions=?''',(user_id, high_score_questions))
    date_of_high_score = cursor.fetchone()[0]
    if date_of_high_score == None:
        date_of_high_score = "2001-11-17"
    connection.commit()
    connection.close()
    return date_of_high_score

def get_outcomes(username, outcome):
    
    '''Outcome can be win, draw or loss'''
    
    if outcome not in ['win', 'draw', 'loss']:
        return {"error": "Invalid outcome type. Must be 'win', 'draw', or 'loss'."}
    
    user_id = check_for_same_username(username)[0][0]
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    query = f'''SELECT COUNT({outcome}) FROM games WHERE user_id=? AND {outcome}=1''' 
    cursor.execute(query, (user_id,))
    outcomes = cursor.fetchone()[0] 
    connection.commit()
    connection.close()
    return outcomes


# def get_wins(username):
    
#     user_id = check_for_same_username(username)[0][0]
#     connection = sqlite3.connect(DATABASE_PATH)
#     cursor = connection.cursor()
#     cursor.execute('''SELECT COUNT(win) from games WHERE user_id=? AND win=?''',(user_id, 1))
#     wins = cursor.fetchone()[0]
#     connection.commit()
#     connection.close()
#     return wins

# def get_draws(username):
    
#     user_id = check_for_same_username(username)[0][0]
#     connection = sqlite3.connect(DATABASE_PATH)
#     cursor = connection.cursor()
#     cursor.execute('''SELECT COUNT(draw) from games WHERE user_id=? AND draw=?''',(user_id, 1))
#     draws = cursor.fetchone()[0]
#     connection.commit()
#     connection.close()
#     return draws

# def get_losses(username):
    
#     user_id = check_for_same_username(username)[0][0]
#     connection = sqlite3.connect(DATABASE_PATH)
#     cursor = connection.cursor()
#     cursor.execute('''SELECT COUNT(loss) from games WHERE user_id=? AND loss=?''',(user_id, 1))
#     losses = cursor.fetchone()[0]
#     connection.commit()
#     connection.close()
#     return losses

def get_all_games():
    
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute('''SELECT * from games''')
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result