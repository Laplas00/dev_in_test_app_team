
class AppSettingsPage:
    def test_open_edit_account_button(self):
        self.logger.info('Start to test "Edit account"')
        self.find_and_click(self.get_res_element_id('edit_account_button'))
        return True
    
    
    def test_photo_changing(self):
        self.logger.info('Start to test "Photo change"')
        self.find_and_click(self.get_res_element_id('upload_image_button'))
        self.click_element_by_xy(350, 1150)
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
        self.scroll_down()
        self.find_and_click(self.get_res_element_id('measurment_change_button'))
        self.find_and_click(self.get_res_element_id('set_ukranian_lang_button'))
        self.find_and_click(self.get_res_element_id('return_back_button'))
        self.open_edit_account()
        self.find_and_click(self.get_res_element_id('measurment_change_button'))
        self.find_and_click(self.get_res_element_id('set_english_lang_button'))
        self.find_and_click(self.get_res_element_id('return_back_button'))
        



