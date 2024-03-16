class SpacePage:
    def test_add_new_space(self, name):
        self.logger.debug('"Start test add new space"')
        self.find_and_click('menu_button')
        self.find_and_click('add_space_button')
        self.find_and_click('name_of_space_field')
        self.el.send_keys(name)
        self.find_and_click('confirm_add_space')
        self.find_element('space_name_interface')

        if self.el.text == name:
            return True
        return False


    def test_delete_space(self):
        self.logger.debug('"Start test delete space"')
        self.find_and_click('settings_in_control_button')

        if self.catch_notification('system_notification'):
            self.logger.info('Notification catched')
            self.swipe_notification('bottom')
            self.test_disable_alarm()
            self.logger.info('Test disable run')
            self.find_and_click('settings_in_control_button')
            
        self.scroll_Y_by_coords(1100, 450)
        self.find_and_click('leave_space_button')
        self.find_and_click('confirm_leave_button')
        self.scroll_down()
        self.find_and_click('checkbox')
        self.find_and_click('confirm_delete_space_button')
        return True
    

    def test_enable_alarm(self):
        self.logger.debug('"Start to test Enable alarm"')
        self.find_and_click('arm_button')
        return True    


    def test_disable_alarm(self):
        self.logger.debug('"Start test Disable alarm"')
        self.find_and_click('disarm_button')
        return True
    

    def test_panic_button(self, till_end):
        self.logger.debug('"Start to test Panic button"')
        self.find_and_click('panic_button')

        if not till_end:
            self.find_and_click('cancel_panic_button')
            return False
        
        else:
            self.find_and_click('cancel_panic_geo_location')
            return True


    def test_night_mode(self):
        self.logger.debug('"Start to test Night mode"')
        self.find_and_click('night_mode_button')
        return True
