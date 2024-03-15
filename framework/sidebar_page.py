import subprocess

from .app_settings_page import AppSettingsPage
from .login_page import LoginPage


class SidebarPage(AppSettingsPage, LoginPage):        
    def test_open_sidebar(self):
        self.logger.info('Start to test "Open sidebar"')
        self.find_and_click(self.get_res_element_id('menu_button'))
        return True

    def test_open_app_settings(self):
        self.logger.info('Start to test "App settings"')
        self.find_and_click(self.get_res_element_id('app_settings_button'))
        return True

    def test_copy_to_clipboard(self):
        command = 'adb shell input tap {} {}'.format('178', '1300')
        subprocess.run(command, shell=True)
        return True
    
    