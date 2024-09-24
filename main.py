import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def user_input():
    user_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if user_choice == "y":
        print(logo)
        add_cards()
    elif user_choice == "n":
        print("Goodbye!")
    else:
        print("Enter a Valid input")
        user_input()

def select_cards(n):
    # Use random.choices to allow duplicates
    random_cards = random.choices(cards, k=n)
    return random_cards

def calculate_score(card_list):
    if sum(card_list) == 21 and len(card_list) == 2:
        return 21  # Blackjack
    if 11 in card_list and sum(card_list) > 21:
        card_list[card_list.index(11)] = 1
    return sum(card_list)

def add_cards():
    random_user_cards = select_cards(2)
    random_comp_cards = select_cards(2)

    user_total = calculate_score(random_user_cards)
    comp_total = calculate_score(random_comp_cards)

    print(f"Your cards are {random_user_cards}, current score: {user_total}")
    print(f"Computer's first card: {random_comp_cards[0]}")

    # Check for immediate Blackjack conditions
    if user_total == 21:
        print("You Won! You got a Blackjack...")
        return
    elif comp_total == 21:
        print("Computer won! Computer had a BlackJack....")
        return
    elif user_total > 21:
        print(f"You Lose!! Your score was :{user_total}")
        return

    # User chooses to draw more cards
    while True:
        user_want_more_cards = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_want_more_cards == "y":
            new_card = select_cards(1)
            random_user_cards.append(new_card[0])
            user_total = calculate_score(random_user_cards)
            print(f"Your cards: {random_user_cards}, current score: {user_total}")

            if user_total > 21:
                print(f"You Lose!! Your score was :{user_total}")
                return
            elif user_total == 21:
                print("You got a Blackjack!")
                return
        elif user_want_more_cards == "n":
            break
        else:
            print("Invalid input! Please type 'y' or 'n'.")

    # Computer's turn to draw cards until it reaches 17 or more
    while comp_total < 17:
        new_comp_card = select_cards(1)
        random_comp_cards.append(new_comp_card[0])
        comp_total = calculate_score(random_comp_cards)

    print(f"Computer's final hand: {random_comp_cards}, final score: {comp_total}")

    # Final comparison
    if comp_total > 21:
        print("Computer went over 21. You WIN!!!")
    elif user_total > comp_total:
        print("You Win😎😎")
    elif comp_total > user_total:
        print("You Lost 😢")
    else:
        print("It's a Draw✌️")

user_input()
user_input()