"""
Check Login Credentials

Password Checker. Created by Chenyuhan Shen. 24-11-2021
"""


def main():
    """Starting Program."""
    password = get_password()
    print(password)
    if check_password(password):
        print("Logged in")
    else:
        print("Illegal access")


def check_password(password):
    """Check if password is valid."""
    return password == "12345678"


def get_password():
    return input("Enter a password")


main()


