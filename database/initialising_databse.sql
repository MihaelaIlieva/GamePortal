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
score INT,
draws INT,
loses INT,
wins INT,
PRIMARY KEY(id),
FOREIGN KEY(user_id) REFERENCES users(id)
)
