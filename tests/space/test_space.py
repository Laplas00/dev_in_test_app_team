import pytest


# ----- Test Creating space ------

@pytest.mark.parametrize("name", ["GOD", "miniTrain", 'School for blind'])
@pytest.mark.order(11)
def test_add_new_space(user_actions, name):
    attempt = user_actions.add_space(name)
    assert attempt == True


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
@pytest.mark.parametrize("is_need_stop, expectation", [(True, True), (False, False)])
def test_panic_button(user_actions, is_need_stop, expectation):
    attempt = user_actions.panic_button(is_need_stop)
    assert attempt == expectation


@pytest.mark.order(16)
def test_night_mode(user_actions):
    attempt = user_actions.night_mode()
    assert attempt == True
