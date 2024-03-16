from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy   
from selenium.common.exceptions import TimeoutException
import subprocess
from utils.android_utils import get_resource_and_text_element_id



class PageWorker:
    '''
        Class contain only functionality 
        to better performance
    '''
    def find_and_click(self, res_id):
        self.find_element(res_id)
        self.el.click()
        self.logger.info('Finding and clicking: [{}]'.format(res_id))


    def text_input(self, text):
        self.clear_text_field()
        adb_command = f'adb shell input text {text}'
        subprocess.run(adb_command, shell=True)


    def get_res_element_id(self, res_id):
        return get_resource_and_text_element_id(res_id)


    def catch_notification(self, element_id):
        try:
            self.logger.info('Attempt to catch notification')
            self.find_element(element_id, sec=3)
            self.logger.warning('Notification found')
            return True
        
        except TimeoutException:
            self.logger.info('No notification found')
            return False
        

    def find_element(self, res_id, sec=8):
        self.logger.info('Finding..: [{}]'.format(res_id))
        el = self.get_res_element_id(res_id)
        self.el = WebDriverWait(self.driver, sec).until(
            EC.presence_of_element_located((
                AppiumBy.XPATH, '//*[{}]'.format(el))))
        self.logger.debug('"Elemnt in self.el : [{}]"'.format(self.el))


    def click_element_by_xy(self, x, y):
        subprocess.run(f'adb shell input tap {x} {y}', shell=True)


    def scroll_down(self):
        for _ in range(3): 
            command = f"adb shell input swipe 500 1100 500 500 300"
            subprocess.run(command, shell=True)


    def scroll_Y_by_coords(self, y_start, y_end):
        adb_command = "adb shell wm size"
        result = subprocess.run(adb_command, shell=True, capture_output=True, text=True)
        output_lines = result.stdout.splitlines()
        screen_size_str = output_lines[-1] 
        screen_width = int(screen_size_str.split(' ')[2].split('x')[0])
        center_x = screen_width // 2
        command = f"adb shell input swipe {center_x} {y_start} {center_x} {y_end} 100"
        subprocess.run(command, shell=True)


    def swipe_notification(self, direction):
        match direction:
            case 'top':
                command = f"adb shell input swipe 150 120 150 500 100"
                subprocess.run(command, shell=True)

            case 'bottom':
                command = f"adb shell input swipe 110 1130 600 1130 100"
                subprocess.run(command, shell=True)


    def clear_text_field(self):
        subprocess.run("adb shell input keyevent KEYCODE_MOVE_END", shell=True)
        coom = 'adb shell input keyevent --longpress $(printf "KEYCODE_DEL %.0s" {25..000})'
        subprocess.run(coom, shell=True)


    def return_home_from_2step_settings(self):
        self.find_and_click('return_back_button')
        self.find_and_click('return_back_button')
        return True
