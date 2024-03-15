
class LogoutPage:    
    def test_logout(self):
        self.find_and_click(self.get_res_element_id('menu_button'))
        self.find_and_click(self.get_res_element_id('app_settings_button'))
        self.scroll_down()
        self.find_and_click(self.get_res_element_id('logout_button'))
        self.logger.info("Attempt to logout success")
        return True  
    
    