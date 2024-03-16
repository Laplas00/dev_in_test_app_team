import subprocess



class LogoutPage:
    def test_logout(self):
        self.logger.debug('"Start test logout"')
        self.find_and_click('menu_button')
        self.find_and_click('app_settings_button')
        command = f"adb shell input swipe 500 1000 500 500 200"
        subprocess.run(command, shell=True)
        self.find_and_click('logout_button')
        self.logger.info("Attempt to logout success")
        self.user_logged_in = False
        return True  
