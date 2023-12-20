"""Logger module"""
import time


class Logger:
    "Logs to file and console with timestamp"

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def log(self, message: str) -> None:
        "Log a message"
        current_time = time.strftime("%H:%M:%S", time.localtime())
        message = f"{current_time} - {message}"
        print(message)
        with open(self.filename, "a", encoding="utf-8") as log_file:
            log_file.write(message + "\n")


class FakeLogger:
    "Stub for Logger"

    def __init__(self) -> None:
        self.messages : list = []

    def log(self, message: str) -> None:
        "Log a message"
        self.messages.append(message)
