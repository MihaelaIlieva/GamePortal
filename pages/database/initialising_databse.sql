CREATE Database game_portal
USE game_portal
CREATE TABLE users(
id INT NOT NULL,
username VARCHAR(30) NOT NULL UNIQUE,
PRIMARY KEY(id)
);
CREATE TABLE game_statistics(
id INT NOT NULL,
user_id INT NOT NULL,
game_name VARCHAR(50) NOT NULL,
max_score INT,
total_draws INT,
total_loses INT,
total_wins INT,
PRIMARY KEY(id),
FOREIGN KEY(user_id) REFERENCES users(id)
)

CREATE TABLE games(
id INT NOT NULL,
user_id INT NOT NULL,
game_name VARCHAR(50) NOT NULL,
date_played DATETIME,
guessed_questions INT,
money_won INT,
win INT,
loss INT,
draw INT,
PRIMARY KEY(id),
FOREIGN KEY(user_id) REFERENCES users(id)
)
