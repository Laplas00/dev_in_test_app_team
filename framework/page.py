from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy   

from utils.android_utils import get_resource_and_text_element_id
from utils import basic_loger



class Page:
    '''
        Я так понимаю что этот класс должен быть абстрактным
        Но конкретно в данной ситуации, это очень странно
        Поэтому в него внес основую логику которая используеться
        в каждом юзабельном классе
    '''
    def __init__(self, driver):
        self.driver = driver
        self.logger = basic_loger.setup_logger('logs.log')


    def get_res_element_id(self, res_id):
        return get_resource_and_text_element_id(res_id)


    def find_element(self, res_id):
        self.el = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                AppiumBy.XPATH, 
                '//*[{}]'.format(res_id))))


    def click_element(self):
        self.el.click()

