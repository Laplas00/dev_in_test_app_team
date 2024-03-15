import pytest
from utils import basic_loger


logger = basic_loger.setup_logger('logs.log')   




<<<<<<< Updated upstream
@pytest.mark.parametrize("username, password, expected_result", [
    ("qa.ajax.app.automation@gmail.com", "qa_automation_password", True),    
    ("invalid_username@gm.co", "invalid_password", False),                   
    ])
def test_correct_login(user_actions, username, password, expected_result):
=======
# @pytest.mark.parametrize("username, password, expected_result", [
#     ("This_is_pass111", "This_is_pass111", True),    
#     ("invalid_username@gm.co", "invalid_password", False),                   
#     ])
# def test_correct_login(user_actions, username, password, expected_result):
>>>>>>> Stashed changes
    
    attempt = user_actions.login(username, password)
    logger.info("Attempt: {}".format(attempt))

    if attempt:
        logger.info("Login success, time to logout ")
        user_actions.reset()

    assert attempt == expected_result

