from .login_page import LoginPage
from .logout_page import LogoutPage
from .sidebar_page import SidebarPage
from .page_worker import PageWorker

from utils import basic_loger



class TestUserUsage(PageWorker, SidebarPage):
    def __init__(self, driver):
        self.driver = driver
        self.logger = basic_loger.setup_logger('user_actions.log')
        self.user_logged_in = False

    def login(self, username, password):
        self.username = username
        self.password = password
        self.attemt_to_login()
        return self.user_logged_in
    
    def logout(self):
        self.check_user_login()
        attempt = self.test_logout()
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
        attempt = self.test_open_edit_account_button()
        return attempt    

    def photo_change(self):
        self.check_user_login()
        attempt = self.test_photo_changing()
        return attempt
    
    def change_name(self):
        self.check_user_login()
        attempt = self.test_name_changing()
        return attempt

    def change_sms_language(self):
        self.check_user_login()
        attempt = self.test_change_sms_language()
        return attempt


