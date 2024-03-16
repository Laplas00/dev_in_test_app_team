import subprocess
import time
import pytest
from appium import webdriver

from utils.android_utils import android_get_desired_capabilities, get_device_udid
from framework.user_actions import TestUserUsage



@pytest.fixture(scope='session')
def run_appium_server():
    f_device_udid = get_device_udid()
    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell', '--udid', f_device_udid],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(5)


@pytest.fixture(scope='session')
def driver(run_appium_server):
    driver = webdriver.Remote('http://localhost:4723', options=android_get_desired_capabilities())
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def user_actions(driver):
    '''
        Создаю основной класс для управления приложением.
        Благодаря лучшей отслеживаемости, могу знать что происходит с приложением
        + не создаю лишние файлы 
    '''
    yield TestUserUsage(driver)
