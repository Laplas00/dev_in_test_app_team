import pytest
from utils import basic_loger


logger = basic_loger.setup_logger('logs.log')   

# Test settings Page

@pytest.mark.order(0)
def test_sidebar_button(user_actions):
    attempt = user_actions.open_sidebar()
    assert attempt == True

@pytest.mark.order(1)
def test_app_setting(user_actions):
    attempt = user_actions.open_app_settings()
    assert attempt == True

@pytest.mark.order(2)
def test_account_edit_button(user_actions):
    attempt = user_actions.open_edit_account()
    assert attempt == True

@pytest.mark.order(3)
def test_photo_changing(user_actions):
    attempt = user_actions.photo_change()
    assert attempt == True

@pytest.mark.order(4)
def test_name_changing(user_actions):
    attempt = user_actions.change_name()
    assert attempt == True


@pytest.mark.order(5)
def test_change_sms_language(user_actions):
    attempt = user_actions.change_sms_language()
    assert attempt == True



# open menu >
# click version 
# click add space
# click name 
# set to Spirutal Help
# press add
# get out notification
# open menu
# press add space
# press upload image
# chose image
# press save
# click name
# input text print('hello world')
# press add 
# get out notification
# press settings
# scroll down
# press leave space button
# press leave
# scroll down
# press checkbox
# confirm delete space
# make cycle until all spaces dont be leaved


# logogut 







# Тест сайдбара:


# press signout > 