from selenium.common.exceptions import TimeoutException
import subprocess

from .page import Page



class LoginPage(Page):
    def attemt_to_login(self):
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
                return False
            
        except TimeoutException:
            self.find_element(self.get_res_element_id('home_page'))
            self.logger.info("Login success")
            self.user_logged_in = True
            return True
    

    def text_input(self, text):
        adb_command = f'adb shell input text "{text}"'
        subprocess.run(adb_command, shell=True)


    def adb_select_all_and_delete(self):
        subprocess.run("adb shell input keyevent KEYCODE_MOVE_END", shell=True)
        coom = 'adb shell input keyevent --longpress $(printf "KEYCODE_DEL %.0s" {25..000})'
        subprocess.run(coom, shell=True)


    def fill_login_fields(self):
        self.find_element(self.get_res_element_id('login_button'))
        self.click_element()
        self.find_element(self.get_res_element_id('login_field_id'))
        self.click_element()
        self.adb_select_all_and_delete()
        self.text_input(self.username)
        self.find_element(self.get_res_element_id('password_field_id'))
        self.click_element()
        self.text_input(self.password)


    def make_login(self):
        self.find_element(self.get_res_element_id('login_button'))
        self.click_element()


    def is_user_login(self):
        return self.user_logged_in



            