# GamePortal
 A university project for Introduction to programming with Python course
 This project is a game portal where a user can login, register, logout, play one of two games - Who wants to be a millionaire and Tic Tac Toe, and view statistics to compare their progress with other users. I used sqlite3 for the database and tkinter for the interface. 
##### The Who wants to be a millionaire game has 15 questions, each has a time limit of 60 seconds to be answered. The user has three lifelines - fifty-fifty (eliminates two wrong options), help from the public (the public votes and gives the answers as percentages) and call a friend (the user connects to an openai prompt where they can ask their question and get answer from there).
##### The Tic Tac Toe is implemented using the minimax algorithm with alpha-beta pruning and depth evaluation so that the machine can make the best move based on the player's move.
