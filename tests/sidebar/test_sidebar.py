import pytest


# ----- Test settings Page ------ 

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
    attempt = user_actions.change_photo()
    assert attempt == True


@pytest.mark.order(4)
def test_name_changing(user_actions):
    attempt = user_actions.change_name()
    assert attempt == True


@pytest.mark.order(5)
def test_change_sms_language(user_actions):
    attempt = user_actions.change_sms_language()
    assert attempt == True


@pytest.mark.order(6)
def test_system_settings_button(user_actions):
    attempt = user_actions.open_system_settings()
    assert attempt == True


@pytest.mark.order(7)
def test_theme_changing(user_actions):
    attempt = user_actions.change_theme()
    assert attempt == True


@pytest.mark.order(8)
def test_change_measurement_units(user_actions):
    attempt = user_actions.change_measurement_units()
    assert attempt == True


@pytest.mark.order(9)
def test_return_to_main_from_deep_settings(user_actions):
    attempt = user_actions.return_home_from_2step_settings()
    assert attempt == True


@pytest.mark.order(10)
def test_copy_to_clipboard(user_actions):
    attempt = user_actions.copy_to_clipboard()
    assert attempt == True


@pytest.mark.order(17)
def test_logoug(user_actions):
    attempt = user_actions.logout()
    assert attempt == True
