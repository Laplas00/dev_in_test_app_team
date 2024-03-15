from selenium.common.exceptions import TimeoutException
from .logout_page import LogoutPage


class LoginPage(LogoutPage):
    def attemt_to_login(self):
        
        self.logger.critical("Fill fields with| {}  {}".format(self.username, self.password))
        self.fill_login_fields()
        self.make_login()
        
        # trying to catch sync err
        try:
            self.find_element(self.get_res_element_id('error_label'))
            if self.el.text == 'Synchronizing with the server, please wait':
                self.logger.info("Syncronizing...")
                self.make_login()
                self.logger.info("Attempt to login")
                self.find_element(self.get_res_element_id('home_page'))
                self.logger.info("Login success after syncronizing")
                self.user_logged_in = True
                return True
            
            elif self.el.text in ('Invalid email format', 'Wrong login or password'):
                self.logger.info(self.el.text)
                self.user_logged_in = False
                return False
            
            else:
                self.logger.error(self.el.text)
                self.user_logged_in = False
                return False
            
        except TimeoutException:
            self.find_element(self.get_res_element_id('home_page'))
            self.logger.info("Login success")
            self.user_logged_in = True
            return True
    

    def fill_login_fields(self):
        self.find_and_click(self.get_res_element_id('login_button'))
        self.find_and_click(self.get_res_element_id('login_field_id'))
        self.clear_text_field()
        self.text_input(self.username)
        self.find_and_click(self.get_res_element_id('password_field_id'))
        self.text_input(self.password)


    def make_login(self):
        self.find_and_click(self.get_res_element_id('login_button'))


    def is_user_login(self):
        return self.user_logged_in



            