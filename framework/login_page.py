from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException

from .page import Page
import subprocess
from utils.basic_loger import setup_logger
from time import sleep



class LoginPage(Page):
    logger = setup_logger('login.log')
    login_button = '@resource-id="com.ajaxsystems:id/text" and @text="Log in"'
    login_field_id = '@resource-id="com.ajaxsystems:id/authLoginEmail"'
    password_field_id = '@resource-id="com.ajaxsystems:id/authLoginPassword"'
    error_label = '@resource-id="com.ajaxsystems:id/snackbar_text"'
    menu_button  = '@resource-id="com.ajaxsystems:id/menuDrawer"'
    app_settings_button = '@resource-id="com.ajaxsystems:id/title" and @text="App settings"'
    logout_button = '@resource-id="com.ajaxsystems:id/title" and @text="Sign out"'
    home_page = '@resource-id="com.ajaxsystems:id/navHostFragment"'

    def attemt_to_login(self, login, password):
        self.login = login
        self.password = password

        self.fill_login_fields()
        self.make_login()

        try:
            self.find_element(self.error_label)

            if self.el.text == 'Synchronizing with the server, please wait':
                self.logger.info("Syncronizing...")
                sleep(4)
                self.make_login()
                self.logger.info("try to login")
                self.find_element(self.home_page)
                self.logger.info("Вход выполнен успешно.")
                self.make_signout()
                return True
            
            elif self.el.text in ('Invalid email format', 'Wrong login or password'):
                self.logger.info(self.el.text)
                return False
        
        except TimeoutException:
            self.find_element(self.home_page)
            self.logger.info("Вход выполнен успешно.")
            self.make_signout()
            return True
    

    def make_signout(self):
        self.find_element(self.menu_button)
        self.click_element()
        self.find_element(self.app_settings_button)
        self.click_element()
        command = f"adb shell input swipe 500 1000 500 500 200"
        subprocess.run(command, shell=True)
        self.find_element(self.logout_button)
        self.click_element()


    def fill_login_fields(self):
        self.find_element(self.login_button)
        self.click_element()
        self.find_element(self.login_field_id)
        self.click_element()
        self.adb_select_all_and_delete()
        self.text_input(self.login)
        self.find_element(self.password_field_id)
        self.click_element()
        self.text_input(self.password)


    def adb_select_all_and_delete(self):
        subprocess.run("adb shell input keyevent KEYCODE_MOVE_END", shell=True)
        coom = 'adb shell input keyevent --longpress $(printf "KEYCODE_DEL %.0s" {25..000})'
        subprocess.run(coom, shell=True)


    def make_login(self):
        self.find_element(self.login_button)
        self.click_element()


    def find_element(self, res_id):
        self.el = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                AppiumBy.XPATH, 
                '//*[{}]'.format(res_id))))


    def click_element(self):
        self.el.click()


    def text_input(self, text):
        adb_command = f'adb shell input text "{text}"'
        subprocess.run(adb_command, shell=True)



# Wrong login or password
# Wrong login or password
# @resource-id="com.ajaxsystems:id/snackbar_text"
            