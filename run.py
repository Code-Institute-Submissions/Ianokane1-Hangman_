import random
import os
from words import dataset


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def print_hangman(values):
    """
    Drawing of the hangman image.
    """
    print()
    print("\t +--------+")
    print("\t |       | |")
    print("\t {}       | |".format(values[0]))
    print("\t{}{}{}      | |".format(values[1], values[2], values[3]))
    print("\t {}       | |".format(values[4]))
    print("\t{} {}      | |".format(values[5], values[6]))
    print("\t         | |")
    print("  _______________|_|___")
    print("  `````````````````````")
    print()


def print_hangman_win():
    """
    Drawing of the hangman image.
    """
    print()
    print("\t +--------+")
    print("\t         | |")
    print("\t         | |")
    print("\t O       | |")
    print("\t/|\\      | |")
    print("\t |       | |")
    print("  ______/_\\______|_|___")
    print("  `````````````````````")
    print()


word_display = []


def print_word(values):
    print()
    print("\t", end="")
    for x in values:
        print(x, end="")
    print()


def check_win(values):
    for char in values:
        if char == "_":
            return False
    return True


def hangman_game(word):
    """
    Get word from words.py, ask user to guess a letter.
    """
    clear()
    word_display = []
    correct_letters = []
    incorrect = []
    chances = 0
    hangman_values = ["O", "/", "|", "\\", "|", "/", "\\"]
    show_hangman_values = [" ", " ", " ", " ", " ", " ", " "]
    for char in word:
        if char.isalpha():
            word_display.append("_")
            correct_letters.append(char.upper())
        else:
            word_display.append(char)

    while True:
        """
        Printed with correct and incorrect display
        """
        clear()
        print_hangman(show_hangman_values)
        print_word(word_display)
        print()
        print("Incorrect characters: ", incorrect)
        print()
# If the user already selected
        inp = input("Enter a character =\n")
        if len(inp) != 1:
            clear()
            print("Wrong choice!! Try Again")
            continue
        if not inp[0].isalpha():
            clear()
            print("Wrong choice!! Try Again")
        if inp.upper() in incorrect:
            clear()
            print("Already tried!!")
            continue
        # If the user runs out of tries:
        if inp.upper() not in correct_letters:
            incorrect.append(inp.upper())
            show_hangman_values[chances] = hangman_values[chances]
            chances = chances + 1
            if chances == len(hangman_values):
                print()
                clear()
                print("\tGame Over!!")
                print_hangman(hangman_values)
                print("The word is :", word.upper())
                break
            # If the user wins and gets the whole word:
        else:
            for i in range(len(word)):
                if word[i].upper() == inp.upper():
                    word_display[i] = inp.upper()
            if check_win(word_display):
                clear()
                print_hangman_win()
                print("\tCongratulations! To play again hit 'Run Program'")
                print("The word is :", word.upper())
                break


if __name__ == "__main__":
    clear()
# game menu to display all three options
    topics = {1: "Football players", 2: "Rockstars", 3: "Marvel Characters"}
    """
    Game Menu display
    """

    while True:
        print()
        print("---------------------")
        print("\t\tHANGMAN")
        print("---------------------")
        for key in topics:
            print("Press", key, "to select", topics[key])
            print()
        try:
            choice = int(input("Enter your choice =\n"))
        except ValueError:
            clear()
            print("Wrong choice!! Try again")
            continue

        if choice > len(topics) + 1:
            clear()
            print("No such topic!! Try again.")
            continue
        elif choice == len(topics) + 1:
            print()
            print("Thank you for playing! To play again hit 'Run Program'")
            break

        chosen_topic = topics[choice]
        ran = random.choice(dataset[chosen_topic])
        hangman_game(ran)
