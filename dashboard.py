def get_user_dashboard(user_name):
    user_dashboard = {
        "username": user_name,
        "status": "Active",
        "message": "Welcome to your dashboard!"
    }
    return user_dashboard


if __name__ == "__main__":
    print(get_user_dashboard("Admin"))
