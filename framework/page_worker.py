from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy   

from utils.android_utils import get_resource_and_text_element_id
from utils.correct_login_data import u, p
import subprocess



class PageWorker:
    def text_input(self, text):
        adb_command = f'adb shell input text "{text}"'
        subprocess.run(adb_command, shell=True)


    def find_and_click(self, res_id):
        self.logger.info('Finding element : [{}]'.format(res_id))
        self.find_element(res_id)
        self.logger.info('Click element : {}'.format(res_id))
        self.click_element()

    def click_element(self):
        self.el.click()

    def get_res_element_id(self, res_id):
        self.logger.debug('Get res element id RUN"')
        return get_resource_and_text_element_id(res_id)
        
            
    def find_element(self, res_id):
        self.el = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                AppiumBy.XPATH, 
                '//*[{}]'.format(res_id))))


    def click_element_by_xy(self, x, y):
        command_to_touch = f'adb shell input tap {x} {y}'
        subprocess.run(command_to_touch, shell=True)
        
        
    def scroll_down(self):
        command = f"adb shell input swipe 500 1000 500 500 200"
        subprocess.run(command, shell=True)
    

    def scroll_by_coords(self, y_start, y_end, duration):
        # scroll by vertical center 
        adb_command = "adb shell wm size"
        result = subprocess.run(adb_command, shell=True, capture_output=True, text=True)
        output_lines = result.stdout.splitlines()
        screen_size_str = output_lines[-1] 
        screen_width = int(screen_size_str.split(' ')[2].split('x')[0])
        center_x = screen_width // 2
        command = f"adb shell input swipe {center_x} {y_start} {center_x} {y_end} {duration}"
        subprocess.run(command, shell=True)

    def clear_text_field(self):
        subprocess.run("adb shell input keyevent KEYCODE_MOVE_END", shell=True)
        coom = 'adb shell input keyevent --longpress $(printf "KEYCODE_DEL %.0s" {25..000})'
        subprocess.run(coom, shell=True)


    def check_user_login(self):
        if self.is_user_login() == False:
            self.login(u, p)

    def reset(self):
        return self.test_logout()
