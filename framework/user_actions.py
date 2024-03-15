from .login_page import LoginPage
from .logout_page import LogoutPage
from .sidebar_page import SidebarPage



class TestUserUsage(LoginPage, LogoutPage, SidebarPage):
    user_logged_in = False
    
    def login(self, username, password):
        self.username = username
        self.password = password
        attempt = self.attemt_to_login()
        return attempt


    def reset(self):
        return self.logout()
	