import subprocess


class SpacePage:
    def test_add_new_space(self, space_name):

        self.find_and_click(self.get_res_element_id('menu_button'))
        self.find_and_click(self.get_res_element_id('add_space_button'))
        self.find_and_click(self.get_res_element_id('name_of_space_field'))

        if len(space_name) == 0:
            comm = "adb shell input keyevent 279"
            clipboard_content = subprocess.check_output(comm, shell=True)
            self.text_input(clipboard_content)
            self.find_and_click(self.get_res_element_id('confirm_add_space'))
            return True

        self.find_and_click(self.get_res_element_id('confirm_add_space'))
        self.text_input(space_name)
        return True

    def test_sound_space(self):
        return True
    
    def test_delete_space(self):
        return True
