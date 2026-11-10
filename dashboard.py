def get_user_dashboard(user_name):
    dashboard = {
        "username": user_name,
        "status": "Active",
        "message": "Welcome to your dashboard!"
    }
    return dashboard

if __name__ == "__main__":
    print(get_user_dashboard("Admin"))
