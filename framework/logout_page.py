from selenium.common.exceptions import TimeoutException
import subprocess

from .page import Page



class LogoutPage(Page):
    def logout(self):
        try:
            self.find_element(self.get_res_element_id('menu_button'))
            self.click_element()
            self.find_element(self.get_res_element_id('app_settings_button'))
            self.click_element()
            command = f"adb shell input swipe 500 1000 500 500 200"
            subprocess.run(command, shell=True)
            self.find_element(self.get_res_element_id('logout_button'))
            self.click_element()
            self.logger.info("Attempt to logout success")
            return True  

        except TimeoutException:
            self.logger.info("Attempt to logout failed")
            return False