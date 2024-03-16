class AppSettingsPage:  
    def test_open_edit_account(self):
        self.logger.debug('"Start test Edit account"')
        self.find_and_click('edit_account_button')
        return True
    

    def test_change_photo(self):
        self.logger.debug('"Start test Photo change"')
        self.find_and_click('upload_image_button')
        self.click_element_by_xy(350, 1150)
        self.scroll_Y_by_coords(500, 800)
        self.find_and_click('save_avatar_image_button')
        return True
        

    def test_change_name(self):
        self.logger.debug('"Start to test Name changing"')
        self.find_and_click('change_name_field')
        self.text_input('OnlyUp')
        self.find_and_click('return_back_button')
        return True


    def test_change_sms_language(self):
        self.logger.debug('"Start test SMS Language"')
        self.open_edit_account()
        self.find_and_click('sms_language_field')
        self.scroll_down()
        self.find_and_click('set_ukranian_lang_button')
        self.find_and_click('return_back_button')
        self.open_edit_account()
        self.find_and_click('sms_language_field')
        self.find_and_click('set_english_lang_button')
        self.find_and_click('return_back_button')
        return True


    def test_open_system_settings(self):
        self.logger.debug('"Start test "Open system settings"')
        self.find_and_click('system_settings_button')
        return True


    def test_change_theme(self):
        self.logger.debug('"Start test Change theme"')
        self.find_and_click('appereance_button')
        self.find_and_click('theme_item2')
        return True


    def test_change_measurement_units(self):
        self.logger.debug('"Start test Change measurement units"')
        self.find_and_click('measurement_unit_chose')
        self.find_and_click('measurement_unit0')
        return True
        