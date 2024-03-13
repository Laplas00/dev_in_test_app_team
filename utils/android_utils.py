from appium.options.android import UiAutomator2Options


def android_get_desired_capabilities(udid):
    options = {   
        'platformName': 'Android',                                      
        'appium:automationName': 'uiautomator2',                               
        'appium:udid': udid,                                         
        'appium:platformVersion': '9',                                         
        'appium:autoGrantPermissions': True,                                   
        'appium:newCommandTimeout': 500,                                       
        'appium:noSign': True,                                                 
        'appium:resetKeyboard': True,                                          
        'appium:systemPort': '8301',                                             
        'appium:appPackage': 'com.ajaxsystems',                                
        'appium:appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity',  
        'appium:takesScreenshot': True                                         
    }
    capabilities_options = UiAutomator2Options().load_capabilities(options)
    return capabilities_options

