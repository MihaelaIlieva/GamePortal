import unittest

from mainpage import MainPage
from loginpage import LoginPage
from getrich import GetRichGame
from tkinter import Tk, Toplevel
from profilepage import ProfilePage
from registerpage import RegisterPage
from tictactoepage import TicTacToeGame
from statisticspage import StatisticsDisplay
from unittest.mock import patch, Mock, MagicMock

class TestMainPage(unittest.TestCase):

    @patch('mainpage.Tk', spec=Tk)
    @patch('mainpage.PhotoImage')
    @patch('mainpage.loginpage.LoginPage')
    def test_open_login_page(self, mock_login_page, mock_photoimage, mock_tk):
        mock_tk_instance = MagicMock()
        mock_tk.return_value = mock_tk_instance

        main_page = MainPage()
        main_page.open_login_page()

        mock_tk_instance.destroy.assert_called_once()
        mock_login_page.assert_called_once()

    @patch('mainpage.Tk', spec=Tk)
    @patch('mainpage.PhotoImage')
    @patch('mainpage.registerpage.RegisterPage')
    def test_open_register_page(self, mock_register_page, mock_photoimage, mock_tk):
        mock_tk_instance = MagicMock()
        mock_tk.return_value = mock_tk_instance

        main_page = MainPage()
        main_page.open_register_page()

        mock_tk_instance.destroy.assert_called_once()
        mock_register_page.assert_called_once()


class TestLoginPage(unittest.TestCase):

    @patch('loginpage.Tk', spec=Tk)
    @patch('loginpage.Entry')
    @patch('loginpage.Label')
    @patch('loginpage.Button')
    @patch('loginpage.PhotoImage')  
    @patch('loginpage.basicqueries.check_for_same_username')  
    @patch('loginpage.basicqueries.get_user_credentials')  
    def test_login_successful(self, mock_get_user_credentials, mock_check_for_same_username, mock_photoimage, mock_button, mock_label, mock_entry, mock_tk):
        mock_tk_instance = MagicMock()
        mock_tk.return_value = mock_tk_instance
        mock_entry.return_value.get.side_effect = ['existing_user', 'correct_password']
        
        # Mocking the database behavior
        mock_check_for_same_username.return_value = [(1,)]  # User exists
        mock_get_user_credentials.return_value = [('existing_user', 'correct_password')]  # Correct credentials

        login_page = LoginPage()
        login_page.login()

        mock_get_user_credentials.assert_called_once_with(1)
        mock_label.return_value.config.assert_called_once_with(text="Successful login!")

    @patch('loginpage.Tk', spec=Tk)
    @patch('loginpage.Entry')
    @patch('loginpage.Label')
    @patch('loginpage.Button')
    @patch('loginpage.PhotoImage')  
    @patch('loginpage.basicqueries.check_for_same_username')  
    @patch('loginpage.basicqueries.get_user_credentials')
    def test_login_invalid_username(self, mock_get_user_credentials, mock_check_for_same_username, mock_photoimage, mock_button, mock_label, mock_entry, mock_tk):
        mock_tk_instance = MagicMock()
        mock_tk.return_value = mock_tk_instance
        mock_entry.return_value.get.side_effect = ['nonexistent_user', 'password']
        
        # Mocking the database behavior
        mock_check_for_same_username.return_value = []  # User does not exist

        login_page = LoginPage()
        login_page.login()

        mock_check_for_same_username.assert_called_once_with('nonexistent_user')
        mock_label.return_value.config.assert_called_once_with(text="No such user!")

    @patch('loginpage.Tk', spec=Tk)
    @patch('loginpage.Entry')
    @patch('loginpage.Label')
    @patch('loginpage.Button')
    @patch('loginpage.PhotoImage')  
    @patch('loginpage.basicqueries.check_for_same_username')  
    @patch('loginpage.basicqueries.get_user_credentials')  
    def test_login_invalid_password(self, mock_get_user_credentials, mock_check_for_same_username, mock_photoimage, mock_button, mock_label, mock_entry, mock_tk):
        mock_tk_instance = MagicMock()
        mock_tk.return_value = mock_tk_instance
        mock_entry.return_value.get.side_effect = ['existing_user', 'wrong_password']
        
        # Mocking the database behavior
        mock_check_for_same_username.return_value = [(1,)]  # User exists
        mock_get_user_credentials.return_value = [('existing_user', 'correct_password')]  # Incorrect password

        login_page = LoginPage()
        login_page.login()

        mock_get_user_credentials.assert_called_once_with(1)
        mock_label.return_value.config.assert_called_once_with(text="Wrong password!")

    @patch('loginpage.Tk', spec=Tk)
    @patch('loginpage.Entry')
    @patch('loginpage.Label')
    @patch('loginpage.Button')
    @patch('loginpage.PhotoImage')  
    @patch('loginpage.basicqueries.check_for_same_username')  
    @patch('loginpage.basicqueries.get_user_credentials')
    def test_login_empty_fields(self, mock_get_user_credentials, mock_check_for_same_username, mock_photoimage, mock_button, mock_label, mock_entry, mock_tk):
        mock_tk_instance = MagicMock()
        mock_tk.return_value = mock_tk_instance
        mock_entry.return_value.get.side_effect = ['', '']
        
        login_page = LoginPage()
        login_page.login()

        mock_label.return_value.config.assert_called_once_with(text="No such user!")


class TestRegisterPage(unittest.TestCase):

    @patch('registerpage.Tk', spec=Tk)
    @patch('registerpage.Entry')
    @patch('registerpage.Label')
    @patch('registerpage.Button')
    @patch('registerpage.PhotoImage')  # Patch PhotoImage class
    @patch('registerpage.basicqueries.check_for_same_username')  # Patching the correct module
    @patch('registerpage.basicqueries.add_user')  # Patching the correct module
    def test_register_successful(self, mock_add_user, mock_check_for_same_username, mock_photoimage, mock_button, mock_label, mock_entry, mock_tk):
        mock_tk_instance = MagicMock()
        mock_tk.return_value = mock_tk_instance
        mock_entry.return_value.get.side_effect = ['new_user', 'new_password']

        # Mocking the database behavior
        mock_check_for_same_username.return_value = False  # Username doesn't exist

        register_page = RegisterPage()
        register_page.register()

        mock_label.return_value.config.assert_called_once_with(text="Successfully registered. Please log in.")

    @patch('registerpage.Tk', spec=Tk)
    @patch('registerpage.Entry')
    @patch('registerpage.Label')
    @patch('registerpage.Button')
    @patch('registerpage.PhotoImage')  # Patch PhotoImage class
    @patch('registerpage.basicqueries.check_for_same_username')  # Patching the correct module
    @patch('registerpage.basicqueries.add_user')  # Patching the correct module
    def test_register_existing_username(self, mock_add_user, mock_check_for_same_username, mock_photoimage, mock_button, mock_label, mock_entry, mock_tk):
        mock_tk_instance = MagicMock()
        mock_tk.return_value = mock_tk_instance
        mock_entry.return_value.get.side_effect = ['existing_user', 'password']

        # Mocking the database behavior
        mock_check_for_same_username.return_value = True  # Username already exists

        register_page = RegisterPage()
        register_page.register()

        mock_label.return_value.config.assert_called_once_with(text="Username already exists. Please choose another one.")

    @patch('registerpage.Tk', spec=Tk)
    @patch('registerpage.Entry')
    @patch('registerpage.Label')
    @patch('registerpage.Button')
    @patch('registerpage.PhotoImage')  # Patch PhotoImage class
    @patch('registerpage.basicqueries.check_for_same_username')  # Patching the correct module
    @patch('registerpage.basicqueries.add_user')  # Patching the correct module
    def test_register_empty_fields(self, mock_add_user, mock_check_for_same_username, mock_photoimage, mock_button, mock_label, mock_entry, mock_tk):
        mock_tk_instance = MagicMock()
        mock_tk.return_value = mock_tk_instance
        mock_entry.return_value.get.side_effect = ['', '']

        register_page = RegisterPage()
        register_page.register()

        mock_label.return_value.config.assert_called_once_with(text="Please fill in all fields.")


class TestProfilePage(unittest.TestCase):

    @patch('profilepage.Tk', spec=Tk)
    @patch('profilepage.Label')
    @patch('profilepage.Button')
    @patch('profilepage.PhotoImage')
    @patch('profilepage.getrich.GetRichGame')
    def test_open_get_rich_page(self, mock_getrich_page, mock_photoimage, mock_button, mock_label, mock_tk):
        mock_tk_instance = MagicMock()
        mock_tk.return_value = mock_tk_instance
        
        profile_page = ProfilePage("Username")
        profile_page.open_get_rich_page()

        mock_tk_instance.destroy.assert_called_once()
        mock_getrich_page.assert_called_once()

    @patch('profilepage.Tk', spec=Tk)
    @patch('profilepage.Label')
    @patch('profilepage.Button')
    @patch('profilepage.PhotoImage')  
    @patch('profilepage.tictactoepage.TicTacToeGame')
    def test_open_tic_tac_toe_page(self, mock_tictactoe_page, mock_photoimage, mock_button, mock_label, mock_tk):
        mock_tk_instance = MagicMock()
        mock_tk.return_value = mock_tk_instance
        
        profile_page = ProfilePage("Username")
        profile_page.open_tic_tac_toe_page()

        mock_tk_instance.destroy.assert_called_once()
        mock_tictactoe_page.assert_called_once()

    @patch('profilepage.Tk', spec=Tk)
    @patch('profilepage.Label')
    @patch('profilepage.Button')
    @patch('profilepage.PhotoImage')
    @patch('profilepage.statisticspage.StatisticsDisplay')  
    def test_open_statistics_page(self, mock_statistics_page, mock_photoimage, mock_button, mock_label, mock_tk):
        mock_tk_instance = MagicMock()
        mock_tk.return_value = mock_tk_instance
        
        profile_page = ProfilePage("Username")
        profile_page.open_statistics_page()

        mock_tk_instance.destroy.assert_called_once()
        mock_statistics_page.assert_called_once()

    @patch('profilepage.Tk', spec=Tk)
    @patch('profilepage.Label')
    @patch('profilepage.Button')
    @patch('profilepage.PhotoImage')  
    @patch('profilepage.mainpage.MainPage')
    def test_open_main_page(self, mock_main_page, mock_photoimage, mock_button, mock_label, mock_tk):
        mock_tk_instance = MagicMock()
        mock_tk.return_value = mock_tk_instance
        
        profile_page = ProfilePage("Username")
        profile_page.open_main_page()

        mock_tk_instance.destroy.assert_called_once()
        mock_main_page.assert_called_once()


class TestGetRichGame(unittest.TestCase):
    @patch('getrich.Tk')
    @patch('getrich.PhotoImage', spec=True)
    def setUp(self, mock_photo_image, mock_tk):
        self.game = GetRichGame("test_user")

    def test_initialization(self):
        self.assertEqual(self.game.username, "test_user")
        self.assertEqual(self.game.timer_seconds, self.game.TIMER_DURATION-1)
        self.assertEqual(self.game.questions_answered, 0)
        self.assertIsInstance(self.game.easy_questions, list)
        self.assertIsInstance(self.game.medium_questions, list)
        self.assertIsInstance(self.game.hard_questions, list)

    def test_get_username(self):
        self.assertEqual(self.game.get_username(), "test_user")

    def test_get_correct_option(self):
        self.game.current_question = "Какво липсва в първия телефонен указател?"
        self.game.first_answer = "Телефонни номера"
        self.game.second_answer = "Година на издаване"
        self.game.third_answer = "Имена на хора"
        self.game.fourth_answer = "Работно време"
        self.assertEqual(self.game.get_correct_option(), "А")

    def test_get_random_percentages(self):
        percentages = self.game.get_random_percentages()
        self.assertIsInstance(percentages, tuple)
        self.assertEqual(len(percentages), 4)
        self.assertEqual(sum(percentages), 100)

    def test_update_timer(self):
        initial_timer = self.game.timer_seconds
        self.game.update_timer()
        self.assertEqual(self.game.timer_seconds, initial_timer - 1)


class TestTicTacToeGame(unittest.TestCase):
    @patch('tictactoepage.Tk')
    def test_is_board_full(self, mock_tk):
        game = TicTacToeGame("test_user")

        self.assertFalse(game.is_board_full())

        # Fill the board
        for i in range(3):
            for j in range(3):
                game.board[i][j] = 'X'

        self.assertTrue(game.is_board_full())

    @patch('tictactoepage.Tk')
    def test_has_winner(self, mock_tk):
        game = TicTacToeGame("test_user")

        self.assertFalse(game.has_winner())

        game.board = [['X', 'X', 'X'],
                      ['.', '.', '.'],
                      ['.', '.', '.']]
        self.assertTrue(game.has_winner())

        game.board = [['O', '.', '.'],
                      ['O', '.', '.'],
                      ['O', '.', '.']]
        self.assertTrue(game.has_winner())

        game.board = [['.', '.', 'X'],
                      ['.', 'X', '.'],
                      ['X', '.', '.']]
        self.assertTrue(game.has_winner())

        game.board = [['O', '.', '.'],
                      ['.', 'O', '.'],
                      ['.', '.', 'O']]
        self.assertTrue(game.has_winner())

    @patch('tictactoepage.Tk')
    def test_evaluate_state(self, mock_tk):
        game = TicTacToeGame("test_user")

        # no winner
        self.assertEqual(game.evaluate_state(), 0)

        # player wins
        game.board = [['X', 'X', 'X'],
                      ['.', '.', '.'],
                      ['.', '.', '.']]
        self.assertEqual(game.evaluate_state(), -10)

        # computer wins
        game.board = [['O', '.', '.'],
                      ['O', '.', '.'],
                      ['O', '.', '.']]
        self.assertEqual(game.evaluate_state(), 10)

        # draw
        game.board = [['X', 'O', 'X'],
                      ['O', 'O', 'X'],
                      ['X', 'X', 'O']]
        self.assertEqual(game.evaluate_state(), 0)

    @patch('tictactoepage.Tk')
    def test_find_best_move(self, mock_tk):
        game = TicTacToeGame("test_user")

        game.board = [['X', 'O', 'X'],
                      ['.', 'O', '.'],
                      ['X', '.', '.']]
        self.assertEqual(game.find_best_move(), (2, 1))

        game.board = [['X', 'X', '.'],
                      ['O', 'O', '.'],
                      ['.', '.', '.']]
        self.assertEqual(game.find_best_move(), (1, 2))

        game.board = [['O', '.', '.'],
                      ['.', 'X', '.'],
                      ['X', '.', '.']]
        self.assertEqual(game.find_best_move(), (0, 2))


if __name__ == '__main__':
    unittest.main()
