from datetime import datetime


def log_message(message):
    timestamp = datetime.now().isoformat(timespec="seconds")
    print(f"[{timestamp}] {message}")


if __name__ == "__main__":
    log_message("Application started")
