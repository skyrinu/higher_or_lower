from art import logo
from art import vs
from game_data import data
from random import choice
from replit import clear


def compare_followers(position_a, position_b):
    if position_a["follower_count"] > position_b["follower_count"]:
        return "a"
    else:
        return "b"


def show_questions(p1, p2):
    print(f"Compare A: {p1['name']}, a {p1['description']}, from {p1['country']}")
    print(vs)
    print(f"Compare B: {p2['name']}, a {p2['description']}, from {p2['country']}")


def higher_or_lower():
    position_a = choice(data)
    position_b = choice(data)
    if position_a == position_b:
        position_b = choice(data)

    score = 0
    game_ends = False

    while not game_ends:
        print(logo)
        has_more_followers = compare_followers(position_a, position_b)
        show_questions(position_a, position_b)

        user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

        if user_input == has_more_followers:
            score += 1
            position_a = position_b
            position_b = choice(data)
            clear()
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, That's wrong answer. Final score {score}.")
            game_ends = True


higher_or_lower()
