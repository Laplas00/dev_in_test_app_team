import pytest
from framework.login_page import LoginPage

from conftest import user_login_fixture


@pytest.mark.parametrize("username, password, expected_result", [
    ("qa.ajax.app.automation@gmail.com", "qa_automation_password", True),    
    ("invalid_username@gm.co", "invalid_password", False),                   
    ])      
def test_correct_login(user_login_fixture, username, password, expected_result):
    attempt = user_login_fixture.attemt_to_login(username, password)
    assert attempt == expected_result

