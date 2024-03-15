from random import randint



class AppSettingsPage:  
    def test_open_edit_account(self):
        self.logger.info('Start to test "Edit account"')
        self.find_and_click(self.get_res_element_id('edit_account_button'))
        return True
    

    def test_change_photo(self):
        self.logger.info('Start to test "Photo change"')
        self.find_and_click(self.get_res_element_id('upload_image_button'))
        self.logger.info('Click for the upload image is set')
        self.click_element_by_xy(350, 1150)
        self.logger.info('Click by cords xy to set photo')
        self.scroll_by_coords(500, 800, 100)
        self.find_and_click(self.get_res_element_id('save_avatar_image_button'))
        return True
        
    def test_name_changing(self):
        self.logger.info('Start to test "Name changing"')
        self.find_and_click(self.get_res_element_id('change_name_field'))
        self.clear_text_field()
        self.text_input('JustBeBetter')
        self.find_and_click(self.get_res_element_id('return_back_button'))
        return True

    def test_change_sms_language(self):
        self.logger.info('Start to test "SMS Language"')
        self.open_edit_account()
        self.find_and_click(self.get_res_element_id('sms_language_field'))
        self.scroll_down()
        self.find_and_click(self.get_res_element_id('set_ukranian_lang_button'))
        self.find_and_click(self.get_res_element_id('return_back_button'))
        self.open_edit_account()
        self.find_and_click(self.get_res_element_id('sms_language_field'))
        self.find_and_click(self.get_res_element_id('set_english_lang_button'))
        self.find_and_click(self.get_res_element_id('return_back_button'))
        return True

    def test_open_system_settings(self):
        self.logger.info('Start to test "Open system settings"')
        self.find_and_click(self.get_res_element_id('system_settings_button'))
        return True


    def test_change_theme(self):
        self.logger.info('Start to test "Change theme"')
        self.find_and_click(self.get_res_element_id('appereance_button'))
        self.find_and_click(self.get_res_element_id('theme_item2'))
        return True


    def test_change_measurement_units(self):
        self.logger.info('Start to test "Change measurement units"')
        self.find_and_click(self.get_res_element_id('measurement_unit_chose'))
        self.find_and_click(self.get_res_element_id('measurement_unit0'))
        
        return True
        
    

