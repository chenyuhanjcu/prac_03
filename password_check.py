"""
Check Login Credentials

Password Checker. Created by Chenyuhan Shen. 24-11-2021
"""
MINIMUM_LENGTH = 8


def main():
    """Starting Program."""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    """Get valid password."""
    password = input(f"Enter password of at least {minimum_length} characters: ")
    while len(password) < minimum_length:
        print("Password too short")
        password = input(f"Enter password of at least {minimum_length} characters: ")
    return password


def print_asterisks(sequence):
    """Print asterisks."""
    print('*' * len(sequence))

main()


