
from dashboard import get_user_dashboard


def test_demo_failure():
    assert 1 == 2

def test_get_user_dashboard():
    result = get_user_dashboard("Admin")

    assert result["username"] == "Admin"
    assert result["status"] == "Active"
    assert result["message"] == "Welcome to your dashboard!"
