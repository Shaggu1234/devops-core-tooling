def authenticate(username, password):
    if username and password:
        return True
    return False

if __name__ == "__main__":
    print(authenticate("admin", "password123"))
