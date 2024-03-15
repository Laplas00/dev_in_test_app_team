from appium.options.android import UiAutomator2Options


elements_id = {
    'login_button'          : '@resource-id="com.ajaxsystems:id/text" and @text="Log in"',
    'login_field_id'        : '@resource-id="com.ajaxsystems:id/authLoginEmail"',
    'password_field_id'     : '@resource-id="com.ajaxsystems:id/authLoginPassword"',
    'error_label'           : '@resource-id="com.ajaxsystems:id/snackbar_text"',
    'menu_button'           : '@resource-id="com.ajaxsystems:id/menuDrawer"',
    'app_settings_button'   : '@resource-id="com.ajaxsystems:id/title" and @text="App settings"',
    'logout_button'         : '@resource-id="com.ajaxsystems:id/title" and @text="Sign out"',
    'home_page'             : '@resource-id="com.ajaxsystems:id/navHostFragment"',}


def get_resource_and_text_element_id(res_id):
    return elements_id[res_id]


def android_get_desired_capabilities():
    options = {   
        'platformName'               : 'Android',                                      
        'appium:automationName'      : 'uiautomator2',                               
        'udid'                       : '320496787230',
        'appium:platformVersion'     : '9',                                         
        'appium:autoGrantPermissions': True,                                   
        'appium:newCommandTimeout'   : 500,                                       
        'appium:noSign'              : True,                                                 
        'appium:resetKeyboard'       : True,                                          
        'appium:systemPort'          : '8301',                                             
        'appium:appPackage'          : 'com.ajaxsystems',                                
        'appium:appActivity'         : 'com.ajaxsystems.ui.activity.LauncherActivity',  
        'appium:takesScreenshot'     : True                                         
    }
    capabilities_options = UiAutomator2Options().load_capabilities(options)
    return capabilities_options

