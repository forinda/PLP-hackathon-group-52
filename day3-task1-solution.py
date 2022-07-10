"""
Door lock system Challenge – Task One (Day 3)
Write a python program that simulates a door lock system such that:
● Password is set and stored in a variable,
● Commands to instruct the door are stored in variables.
● When a user enters the wrong password an error message is displayed and prompted to
enter the password again.
● When a user enters “open” a “The door is now open” statement is displayed, when the
“open” is entered more that once, a message is displayed saying, “the door is already
open”
● When a user enters “close” a “The door is now locked” statement is displayed, when the
“open” is entered more that once, a message is displayed saying, “the door is already
locked”
● When a user enters “quit” the process is terminated and message is displayed.
● When a wrong message is entered or invalid key pressed a “Invalid input” message is
displayed.
● When the door is locked or open, it prints out the last date/time the door was opened, eg
“Door Last open at 2022-07-05 08:46:20.535395”
"""
from datetime import datetime
from getpass import getpass
from time import sleep, time


def logger_decorator(func):
    """Decorator for logging current executing function"""
    def wrapper(*args, **kwargs):
        with open('door-lock-logs.log', '+a') as f:
            f.writelines(
                f"*Running {func.__name__} method -  on {datetime.now().strftime('%A %d. %B %Y %H:%M:%S')}\n")
        print('-' * 50)
        print("Running {} function".format(func.__name__))
        print("-" * 50)
        return func(*args, **kwargs)
    return wrapper


def timer(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        with open('bench-mark-logs.log', '+a') as f:
            f.write(
                f'*Function {func.__name__!r} executed in {(t2-t1):.4f}s\n')
        return result
    return wrap_func


class DoorLock:
    """
Door lock implementation instantiating the class\n
`lock = DoorLock("1234") ` or `lock = DoorLock` the password is optional
so \nif you wish to change the password you can do so using the instance\n 
method setter i.e `lock.password="password"`
    """

    def __init__(self, password="1234") -> None:
        self._commands: dict = {"open": "open", "quit": "quit",
                                "close": "close", "help": ["help", "--help", "-h"]}
        self._password: str = password
        self._is_auth: bool = False
        self._is_locked: bool = True
        self._running: bool = True

    @property
    def commands(self) -> dict:
        return self._commands

    @property
    @timer
    def running(self) -> bool:
        return self._running

    @running.setter
    @timer
    def running(self, value: bool) -> None:
        self._running = value

    @property
    @timer
    def locked(self) -> bool:
        return self._is_locked

    @locked.setter
    @timer
    def locked(self, value: bool) -> None:
        self._is_locked = value

    @property
    @timer
    def password(self) -> str:
        return self._password

    @property
    def auth(self) -> bool:
        return self._is_auth

    @auth.setter
    def auth(self, value: bool) -> None:
        self._is_auth = value

    @password.setter
    def password(self, value: str) -> None:
        self._password = value

    @timer
    @logger_decorator
    def unlock_door(self):
        # Unlock locked door
        self.locked = False

    @timer
    @logger_decorator
    def lock_door(self):
        # Lock unlocked door
        self.locked = True

    @staticmethod
    @timer
    @logger_decorator
    def help():
        h = """
For help commands use:
close - Close door
open - Open door
quit - Terminate program
        """
        print(h)

    @staticmethod
    @timer
    @logger_decorator
    def print_date() -> None:
        # print current date and time
        return datetime.now()

    @logger_decorator
    def main(self):
        """
Main function that executes the logic for opening the door and closing the door
This runs on an endless loop to execute user commands and produce the required output

        """
        print(""" Welcome to automated door locking system """.center(80, "*"))
        while self.running:
            while not self.auth:
                password = getpass(
                    "Take note that password input is hidden\nEnter your password to continue hint: \nUse password used for class object instantiation: ")
                if not password == self.password:
                    print("Invalid password please try again..")
                    continue
                else:
                    self.auth = True
            commands = self.commands.values()
            msg = "[enter command]> "
            user_command = input(msg).lower().strip()
            if user_command in self.commands['help']:
                self.__class__.help()

            elif(user_command not in commands):
                print("Invalid input. use for -h or --help or help")

            elif user_command == self._commands['quit']:
                print(f"Door Last open at {self.__class__.print_date()}")
                self.running = False

            elif user_command == self.commands['open']:
                if not self.locked:
                    print("the door is already open".title())

                else:
                    self.unlock_door()
                    print("The door is now open")
            elif user_command == self.commands['close']:
                if self.locked:
                    print("Door is already locked")
                else:
                    self.lock_door()
                    print("The door is now locked")

    @staticmethod
    @timer
    @logger_decorator
    def run():
        # Run method to execute and abstract the door simulation functionality
        # The password passed to the constructor is the default during object
        # instantiation or it can be overriden by an accessor
        try:
            door_lock = DoorLock("12345")
            door_lock.main()
        except KeyboardInterrupt:
            print("\n\nCTRL + C closing terminal... in 2 seconds\n")
            sleep(2)
        except KeyError:
            print("Key error.....")


if __name__ == "__main__":
    DoorLock.run()
