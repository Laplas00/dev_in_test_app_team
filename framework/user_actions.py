from .sidebar_page import SidebarPage
from .worker_page import PageWorker
from .space_page import SpacePage

from utils import basic_loger



class TestUserUsage(PageWorker, SidebarPage, SpacePage):
    def __init__(self, driver):
        self.driver = driver
        self.logger = basic_loger.setup_logger('user_actions.log')
        self.user_logged_in = False


    def login(self, username, password):
        self.username = username
        self.password = password
        attempt = self.attempt_to_login()
        return attempt
    

    def open_sidebar(self):
        self.check_user_login()
        attempt = self.test_open_sidebar()
        return attempt
    
    def open_app_settings(self):
        self.check_user_login()
        attempt = self.test_open_app_settings()
        return attempt
    
    def open_edit_account(self):
        self.check_user_login()
        attempt = self.test_open_edit_account()
        return attempt
    
    
    def open_system_settings(self):
        self.check_user_login()
        attempt = self.test_open_system_settings()
        return attempt
    
    def change_photo(self):
        self.check_user_login()
        attempt = self.test_change_photo()
        return attempt
        

    def change_theme(self):
        self.check_user_login()
        attempt = self.test_change_theme()
        return attempt

    def change_measurement_units(self):
        self.check_user_login()
        attempt = self.test_change_measurement_units()
        return attempt
    

    # work with spaces
    def add_space(self, space_name):
        self.check_user_login()
        attempt = self.test_add_new_space(space_name)
        return attempt
    
    def delete_space(self):
        self.check_user_login()
        attempt = self.test_delete_space()
        return attempt
    
    def enable_alarm(self):
        self.check_user_login()
        attempt = self.test_enable_alarm()
        return attempt
    
    def disable_alarm(user_actions):
        attempt = user_actions.test_disable_alarm()
        assert attempt == True


    def panic_button(user_actions):
        attempt = user_actions.test_panic_button()
        assert attempt == True


    def night_mode(user_actions):
        attempt = user_actions.test_night_mode()
        assert attempt == True


    def copy_to_clipboard(self):
        self.check_user_login()
        attempt = self.test_copy_to_clipboard()
        return attempt
        

    def reset(self):
        return self.logout()
	
