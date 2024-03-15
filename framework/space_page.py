import subprocess
import time

class SpacePage:
    def test_add_new_space(self, space_name):
        self.logger.info('Start to test "Add new space"')

        self.find_and_click(self.get_res_element_id('menu_button'))
        self.logger.warning(f'{space_name} - Space Name2')
        self.find_and_click(self.get_res_element_id('add_space_button'))
        self.logger.warning(f'{space_name} - Space Name3')
        self.find_and_click(self.get_res_element_id('name_of_space_field'))

        self.logger.warning(f'{space_name} - Clicks ends')
        if not space_name:
            self.logger.warning('Loger not space_name')
            comm = "adb shell input keyevent 279"
            clipboard_content = subprocess.check_output(comm, shell=True, stderr=subprocess.PIPE)
            self.logger(f'{clipboard_content} - clipboard')
            if not clipboard_content:
                self.logger.warning('burabora')

                self.text_input('buraBora')
            
            self.text_input(clipboard_content)
            self.find_and_click(self.get_res_element_id('confirm_add_space'))
            self.logger.warning('return False')

            return False
        

        self.logger.warning('space name passes')
        self.text_input(space_name)
        self.find_and_click(self.get_res_element_id('confirm_add_space'))
        self.logger.warning('return True')
        return True


    def test_delete_space(self):
        self.logger.info('Start to test "Delete space"')
        self.find_and_click(self.get_res_element_id('settings_in_control_button'))
        self.scroll_by_coords(1000, 300, 0.1)
        self.find_and_click(self.get_res_element_id('leave_space_button'))
        self.find_and_click(self.get_res_element_id('leave_confirma_text'))
        self.find_and_click(self.get_res_element_id('leave_confirma_text'))
        self.scroll_by_coords(1000, 300, 0.1)
        self.find_and_click(self.get_res_element_id('checkbox'))
        self.find_and_click(self.get_res_element_id('confirm_delete_space_button'))
        return True
    

    def test_enable_alarm(self):
        self.logger.info('Start to test "Enable alarm"')
        self.find_and_click(self.get_res_element_id('arm_button'))
        return True
    

    def test_disable_alarm(self):
        self.logger.info('Start to test "Disable alarm"')
        self.find_and_click(self.get_res_element_id('disarm_button'))
        return True
    

    def test_panic_button(self, till_end=False):
        self.logger.info('Start to test "Panic button"')
        self.find_and_click(self.get_res_element_id('panic_button'))
        if not till_end:
            self.find_and_click(self.get_res_element_id('cancel_panic_button'))
        else:
            time.sleep(2)
            return True
    

    def test_night_mode(self):
        self.logger.info('Start to test "Night mode"')
        self.find_and_click(self.get_res_element_id('night_mode_button'))
        return True
    
