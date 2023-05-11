import random

def get_valid_input(message):
    while True:
        user_input = input(message)
        if user_input.isdigit():
            return int(user_input)
        else:
            print('Please type a positive integer.')

def play_game(top_of_range, max_guesses, hint_range):
    random_number = random.randint(0, top_of_range)
    guesses = 0
    previous_guesses = []

    while True:
        guesses += 1
        user_guess = get_valid_input("Make a guess: ")
        
        if user_guess in previous_guesses:
            print("You already guessed that number. Try again.")
        elif user_guess == random_number:
            print("You got it!")
            break
        elif user_guess > random_number:
            print("Lower!!!")
            if user_guess - random_number <= hint_range:
                print("Hint: You're very close to the number!")
        else:
            print("Higher!!!")
            if random_number - user_guess <= hint_range:
                print("Hint: You're very close to the number!")
        
        previous_guesses.append(user_guess)
        if guesses == max_guesses:
            print("Sorry, you ran out of guesses. The number was", random_number)
            break

    print("You guessed the number in", guesses, "guesses.")

def choose_difficulty():
    while True:
        print("Choose your difficulty level:")
        print("1. Easy (0-20, 10 guesses, hint range of 5)")
        print("2. Medium (0-50, 8 guesses, hint range of 10)")
        print("3. Hard (0-500, 6 guesses, hint range of 20)")
        print("4. Custom")
        difficulty_choice = get_valid_input("Enter 1, 2, 3, or 4: ")
        
        if difficulty_choice == 1:
            top_of_range = 20
            max_guesses = 10
            hint_range = 5
            break
        elif difficulty_choice == 2:
            top_of_range = 50
            max_guesses = 8
            hint_range = 10
            break
        elif difficulty_choice == 3:
            top_of_range = 500
            max_guesses = 6
            hint_range = 20
            break
        elif difficulty_choice == 4:
            top_of_range = get_valid_input("Type the maximum number: ")
            max_guesses = 20
            hint_range = 5
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

    print("You have chosen difficulty level", difficulty_choice)
    print("The maximum number is", top_of_range)
    return top_of_range, max_guesses, hint_range

top_of_range, max_guesses, hint_range = choose_difficulty()
play_game(top_of_range, max_guesses, hint_range)
