import pytest
from utils.correct_login_data import u, p


email, password = u, p 

@pytest.mark.order(18)
@pytest.mark.parametrize("username, password, expected_result", [
    ("invalid_username@gm.co", "invalid_password", False),                   
    (email, password, True),    
    ])
def test_correct_login(user_actions, username, password, expected_result):    
    if user_actions.user_logged_in:
        user_actions.logout()
    attempt = user_actions.login(username, password)
    assert attempt == expected_result

