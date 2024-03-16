from .sidebar_page import SidebarPage
from .worker_page import PageWorker
from .space_page import SpacePage
from utils import basic_loger


class TestUserUsage(PageWorker, SidebarPage, SpacePage):
    '''Main working class to make tests'''
    def __init__(self, driver):
        self.driver = driver
        self.logger = basic_loger.setup_logger('user_actions.log')
        self.user_logged_in = False


    def login(self, username, password):
        self.username = username
        self.password = password
        attempt = self.test_login()
        return attempt


    def logout(self):
        return self.test_logout()
	
    # ----- sidebar ----- 
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


    def change_name(self):
        self.check_user_login()
        attempt = self.test_change_name()
        return attempt
    

    def change_sms_language(self):
        self.check_user_login()
        attempt = self.test_change_sms_language()
        return attempt


    def change_theme(self):
        self.check_user_login()
        attempt = self.test_change_theme()
        return attempt


    def change_measurement_units(self):
        self.check_user_login()
        attempt = self.test_change_measurement_units()
        return attempt

    # ---- work with spaces ----- #
    def add_space(self, name):
        self.check_user_login()
        attempt = self.test_add_new_space(name)
        return attempt
    

    def delete_space(self):
        self.check_user_login()
        attempt = self.test_delete_space()
        return attempt
    

    def enable_alarm(self):
        self.check_user_login()
        attempt = self.test_enable_alarm()
        return attempt
    

    def disable_alarm(self):
        self.check_user_login()
        attempt = self.test_disable_alarm()
        return attempt


    def panic_button(self, is_need_stop):
        self.check_user_login()
        attempt = self.test_panic_button(is_need_stop)
        return attempt


    def night_mode(self):
        self.check_user_login()
        attempt = self.test_night_mode()
        return attempt


    def copy_to_clipboard(self):
        self.check_user_login()
        attempt = self.test_copy_to_clipboard()
        return attempt
