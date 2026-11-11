from dashboard import get_user_dashboard


def test_dashboard_returns_expected_data():
    result = get_user_dashboard("Admin")

    assert isinstance(result, dict)
    assert result["username"] == "Admin"
    assert result["status"] == "Active"
    assert result["message"] == "Welcome to your dashboard!"
