import random
import os


def clear():
    os.system("clear")


def print_hangman(values):
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
        clear()
        print_hangman(show_hangman_values)
        print_word(word_display)
        print()
        print("Incorrect characters: ", incorrect)
        print()

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
        else:
            for i in range(len(word)):
                if word[i].upper() == inp.upper():
                    word_display[i] = inp.upper()
            if check_win(word_display):
                clear()
                print("\tCongratulations!")
                print_hangman_win()
                print("The word is :", word.upper())
                break


if __name__ == "__main__":
    clear()

    topics = {1: "Football players", 2: "Rockstars", 3: "Marvel Characters"}

    dataset = {
        "Football players": [
            "MO SALAH",
            "LIONEL MESSI",
            "KEVIN DE BRUYNE",
            "CRISTIANO RONALDO",
            "NGOLO KANTE",
            "KYLIAN MBAPPE",
            "NEYMAR",
            "KARIM BENZEMA", 
            "DANI ALVES",
            "ZLATAN IBRAHIMOVIC",
        ],
        "Rockstars": [
            "LIAM GALLAGHER",
            "AXEL ROSE",
            "ERIC CLAPTON",
            "SLASH",
            "PAUL MCCARTNEY",
            "MICK JAGGER",
            "OZZY OSBOURNE",
            "JIMI HENDRIX",
            "BRUCE SPRINGSTEEN",
            "JOHN LENNON",
            "DAVID BOWIE",
        ],
        "Marvel Characters": [
            "CAPTAIN AMERICA",
            "IRON MAN",
            "THANOS",
            "HAWKEYE",
            "BLACK PANTHER",
            "BLACK WIDOW",
            "SPIDERMAN",
            "STARLORD",
            "THOR",
            "DOCTOR STRANGE",
        ],
    }

    while True:
        print()
        print("---------------------")
        print("\t\tGAME MENU")
        print("---------------------")
        for key in topics:
            print("Press", key, "to select", topics[key])
            print("Press", len(topics) + 1, "to quit")
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
            print("Thank you for playing!")
            break

        chosen_topic = topics[choice]
        ran = random.choice(dataset[chosen_topic])
        hangman_game(ran)