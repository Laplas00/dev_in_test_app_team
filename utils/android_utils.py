from appium.options.android import UiAutomator2Options
from .resources_id import elements_id
import subprocess



def android_get_desired_capabilities():
    options = {   
        'platformName'               : 'Android',                                      
        'appium:automationName'      : 'uiautomator2',                               
        'appium:platformVersion'     : '9',                                         
        'appium:autoGrantPermissions': True,                                   
        'appium:newCommandTimeout'   : 500,                                       
        'appium:noSign'              : True,                                                 
        'appium:resetKeyboard'       : True,                                          
        'appium:systemPort'          : '8301',                                             
        'appium:appPackage'          : 'com.ajaxsystems',                                
        'appium:appActivity'         : 'com.ajaxsystems.ui.activity.LauncherActivity',  
        'appium:takesScreenshot'     : True }
    
    capabilities_options = UiAutomator2Options().load_capabilities(options)
    return capabilities_options


def get_device_udid():
    result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
    devices_output = result.stdout.strip().split('\n')[1:] 

    if not devices_output:
        raise RuntimeError("No connected devices found.")
    
    first_device = devices_output[0].split('\t')[0]
    return first_device


def get_resource_and_text_element_id(res_id):
    return elements_id[res_id]
