from selenium.common.exceptions import TimeoutException
import subprocess

from .logout_page import LogoutPage


class LoginPage(LogoutPage):
    def attempt_to_login(self):
        self.find_and_click(self.get_res_element_id('login_button'))
        self.fill_login_fields()
        self.find_and_click(self.get_res_element_id('login_button'))
        
        # trying to catch sync err
        try:
            self.find_element(self.get_res_element_id('error_label'))
            if self.el.text == 'Synchronizing with the server, please wait':
                self.logger.info("Syncronizing...")
                self.find_and_click(self.get_res_element_id('login_button'))
                self.logger.info("Attempt to login")
                self.find_element(self.get_res_element_id('home_page'))
                self.logger.info(f'Element that i fount is {self.el}')

                self.logger.info("Login success after syncronizing")
                self.user_logged_in = True
                return True
            
            elif self.el.text in ('Invalid email format', 'Wrong login or password'):
                self.logger.info(self.el.text)
                self.user_logged_in = False
                return False
            
            else:
                self.logger.error(self.el.text)
                return False
            
        except TimeoutException:
            self.find_element(self.get_res_element_id('home_page'))
            self.logger.info("Login success")
            self.user_logged_in = True
            return True
    

    def adb_select_all_and_delete(self):
        subprocess.run("adb shell input keyevent KEYCODE_MOVE_END", shell=True)
        coom = 'adb shell input keyevent --longpress $(printf "KEYCODE_DEL %.0s" {25..000})'
        subprocess.run(coom, shell=True)


    def fill_login_fields(self):
        self.adb_select_all_and_delete()
        self.find_and_click(self.get_res_element_id('login_field_id'))
        self.text_input(self.username)
        self.find_and_click(self.get_res_element_id('password_field_id'))
        self.text_input(self.password)




            