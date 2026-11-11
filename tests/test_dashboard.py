<<<<<<< HEAD
=======

>>>>>>> f0de1034a291e5adf075b6c5761bd07b02ab415b
from dashboard import get_user_dashboard


def test_get_user_dashboard():
    result = get_user_dashboard("Admin")

    assert result["username"] == "Admin"
    assert result["status"] == "Active"
<<<<<<< HEAD
    assert result["message"] == "Welcome to your dashboard!"
=======
    assert result["message"] == "Welcome to your dashboard!"
>>>>>>> f0de1034a291e5adf075b6c5761bd07b02ab415b
