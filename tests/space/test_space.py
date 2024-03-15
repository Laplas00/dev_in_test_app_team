import pytest

   
        
# Test Creating space

@pytest.mark.order(11)
@pytest.mark.parametrize("space_name, expected_result", [
    ('Hello world', True), 
    ('GOD HERE', True), 
    ('', False)])
def test_add_new_space(user_actions, space_name, expected_result):
    attempt = user_actions.add_space(space_name)
    assert attempt == expected_result


@pytest.mark.order(12)
def test_delete_space(user_actions):
    attempt = user_actions.delete_space()
    assert attempt == True


@pytest.mark.order(13)
def test_enable_alarm(user_actions):
    attempt = user_actions.enable_alarm()
    assert attempt == True


@pytest.mark.order(14)
def test_disable_alarm(user_actions):
    attempt = user_actions.disable_alarm()
    assert attempt == True


@pytest.mark.order(15)
@pytest.mark.parametrize("cancel", [True, False])
def test_panic_button(user_actions, cancel):
    attempt = user_actions.panic_button(cancel)
    assert attempt == True


@pytest.mark.order(16)
def test_night_mode(user_actions):
    attempt = user_actions.night_mode()
    assert attempt == True

