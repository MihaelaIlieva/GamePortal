import unittest
from tkinter import Tk
from mainpage import MainPage
from loginpage import LoginPage
from profilepage import ProfilePage
from registerpage import RegisterPage
from unittest.mock import patch, MagicMock

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


if __name__ == '__main__':
    unittest.main()
