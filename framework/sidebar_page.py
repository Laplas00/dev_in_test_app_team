import subprocess
from .app_settings_page import AppSettingsPage
from .login_page import LoginPage
from .logout_page import LogoutPage



class SidebarPage(AppSettingsPage, LoginPage, LogoutPage):        
    def test_open_sidebar(self):
        self.logger.debug('"Start test Open sidebar"')
        self.find_and_click('menu_button')
        return True


    def test_open_app_settings(self):
        self.logger.debug('"Start test app settings"')
        self.find_and_click('app_settings_button')
        return True


    def test_copy_to_clipboard(self):
        self.logger.debug('"Start test copy to clipboard"')
        command = 'adb shell input tap {} {}'.format('178', '1300')
        subprocess.run(command, shell=True)
        return True
