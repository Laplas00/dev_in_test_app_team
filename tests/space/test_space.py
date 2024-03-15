import pytest

   
        
# Test Creating space

@pytest.mark.order(11)
@pytest.mark.parametrize("space_name", ['Hello world', 'GOD HERE'])
def test_add_new_space(user_actions, space_name):
    attempt = user_actions.add_space(space_name)
    assert attempt == True

# @pytest.mark.order(1)
# def test_app_setting(user_actions):
#     attempt = user_actions.open_app_settings()
#     assert attempt == True

