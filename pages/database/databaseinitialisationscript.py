import sqlite3

connection = sqlite3.connect('game_portal.db')

cursor = connection.cursor()

cursor.execute(
    '''CREATE TABLE users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(30) NOT NULL UNIQUE,
        password VARCHAR(30) NOT NULL
    )
    '''
)

cursor.execute(
    '''CREATE TABLE game_statistics(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        max_score INTEGER,
        total_draws INTEGER,
        total_loses INTEGER,
        total_wins INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    '''
)

cursor.execute(
    '''CREATE TABLE games(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        game_name VARCHAR(50) NOT NULL,
        date_played DATETIME,
        guessed_questions INTEGER,
        money_won INTEGER,
        win INTEGER,
        loss INTEGER,
        draw INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )

    '''
)

connection.commit()
connection.close()