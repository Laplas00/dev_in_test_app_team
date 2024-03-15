from .sidebar_page import SidebarPage
<<<<<<< Updated upstream



class TestUserUsage(LoginPage, LogoutPage, SidebarPage):
    user_logged_in = False
    
=======
from .worker_page import PageWorker
from .space_page import SpacePage

from utils import basic_loger



class TestUserUsage(PageWorker, SidebarPage, SpacePage):
    def __init__(self, driver):
        self.driver = driver
        self.logger = basic_loger.setup_logger('user_actions.log')
        self.user_logged_in = False

>>>>>>> Stashed changes
    def login(self, username, password):
        self.username = username
        self.password = password
        attempt = self.attemt_to_login()
        return attempt
    
    def open_system_settings(self):
        self.check_user_login()
        attempt = self.test_open_system_settings()
        return attempt

    def change_theme(self):
        self.check_user_login()
        attempt = self.test_change_theme()
        return attempt

    def change_measurement_units(self):
        self.check_user_login()
        attempt = self.test_change_measurement_units()
        return attempt
    
    def add_space(self, space_name):
        self.check_user_login()
        attempt = self.test_add_new_space(space_name)
        return attempt
    
    def copy_to_clipboard(self):
        self.check_user_login()
        attempt = self.test_copy_to_clipboard()
        return attempt
        

    def reset(self):
        return self.logout()
	