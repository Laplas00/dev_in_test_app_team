from time import sleep
from utils.correct_login_data import u, p



class LoginPage:
    def test_login(self):
        self.logger.debug('"Start test login"')
        self.find_and_click('login_button')
        self.fill_login_fields()
        self.find_and_click('login_button')

        if not self.catch_notification('error_label'):
            self.find_element('home_page')
            self.logger.info("Login success")
            self.user_logged_in = True
            return True
        
        elif self.el.text == 'Synchronizing with the server, please wait':
            self.logger.info("Syncronizing...")
            sleep(3)
            self.find_and_click('login_button')
            self.find_element('home_page')
            self.logger.info("Login success after sync")
            self.user_logged_in = True
            return True
        
        elif self.el.text in ('Invalid email format', 'Wrong login or password'):
            self.logger.debug(f'"Login: {self.el.text}"')
            self.user_logged_in = False
            return False
        
        else:
            self.logger.error(self.el.text)
            return False
    

    def check_user_login(self):
        if self.user_logged_in == False:
            self.login(u, p)


    def fill_login_fields(self):
        self.find_and_click('login_field_id')
        self.text_input(self.username)
        self.find_and_click('password_field_id')
        self.text_input(self.password)
