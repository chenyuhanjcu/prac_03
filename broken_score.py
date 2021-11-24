"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    """Starting Program."""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    grade = determine_grade(score)
    print(grade)
    random_score = random.randint(0, 101)
    grade = determine_grade(random_score)
    print(f"{random_score} is {grade}")


def determine_grade(score):
    """Determine grade based on score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
