from appium.options.android import UiAutomator2Options


elements_id = {
    'confirm_leave_button'          : '@text="LEAVE"', # i dont like variable with resource_id and text, but i dont have time to change all of this now)
    'checkbox_to_leave'             : '@resource-id="select"',
    'save_avatar_image_button'      : '@resource-id="com.ajaxsystems:id/save"',
    'return_back_button'            : '@resource-id="com.ajaxsystems:id/back"',
    'version_of_build'              : '@resource-id="com.ajaxsystems:id/build"',
    'upload_image_button'           : '@resource-id="com.ajaxsystems:id/upload"',
    'add_space_button'              : '@resource-id="com.ajaxsystems:id/addSpace"',
    'menu_button'                   : '@resource-id="com.ajaxsystems:id/menuDrawer"',
    'error_label'                   : '@resource-id="com.ajaxsystems:id/snackbar_text"',
    'name_of_space_field'           : '@resource-id="com.ajaxsystems:id/inputAddSpace"',
    'login_field_id'                : '@resource-id="com.ajaxsystems:id/authLoginEmail"',
    'settings_in_space_button'      : '@resource-id="com.ajaxsystems:id/buttonSettings"',
    'home_page'                     : '@resource-id="com.ajaxsystems:id/dashboardNavBarFragment"',
    'password_field_id'             : '@resource-id="com.ajaxsystems:id/authLoginPassword"',
    'change_name_field'             : '@resource-id="com.ajaxsystems:id/accountSettingsName"',
    'change_appereance_button'      : '@resource-id="com.ajaxsystems:id/appSettingsAppearance"',
    'confirm_add_space'             : '@resource-id="com.ajaxsystems:id/topBarActionTextButton"',
    'dark_appereance_button'        : '@resource-id="com.ajaxsystems:id/title" and @text="Dark"',
    'login_button'                  : '@resource-id="com.ajaxsystems:id/text" and @text="Log in"',
    'logout_button'                 : '@resource-id="com.ajaxsystems:id/title" and @text="Sign out"',
    'sessions_button'               : '@resource-id="com.ajaxsystems:id/title" and @text="Sessions"',
    'set_english_lang_button'       : '@resource-id="com.ajaxsystems:id/textView" and @text="English"',
    'measurment_change_button'      : '@resource-id="com.ajaxsystems:id/appSettingsMeasurementSystem"',
    'confirm_detele_space_button'   : '@resource-id="com.ajaxsystems:id/text" and @text="Delete space"',
    'leave_space_button'            : '@resource-id="com.ajaxsystems:id/title" and @text="Leave space"',
    'edit_account_button'           : '@resource-id="com.ajaxsystems:id/title" and @text="Edit account"',
    'app_settings_button'           : '@resource-id="com.ajaxsystems:id/title" and @text="App settings"',
    'set_ukranian_lang_button'      : '@resource-id="com.ajaxsystems:id/textView" and @text="Українська"',
    'system_settings_button'        : '@resource-id="com.ajaxsystems:id/title" and @text="System settings"',
    'account_protection_button'     : '@resource-id="com.ajaxsystems:id/title" and @text="Account protection"',
    'imperial_chose_button'         : '@resource-id="com.ajaxsystems:id/textView" and @text="Imperial/US customary"',
    
    }


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

