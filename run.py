import os
import random

def clear():
    os.system("cls")

def print_hangman(vaulues):
    print()
    print("\t +--------+")
    print("\t |       | |")
    print("\t {}       | |".format(values[0]))
    print("\t{}{}{}      | |".format(values[1], values[2], values[3]))
    print("\t {}       | |".format(values[4]))
    print("\t{} {}      | |".format(values[5],values[6]))
    print("\t         | |")
    print("  _______________|_|___")
    print("  `````````````````````")
    print()  

def hangman_game(word):
    clear()
    word_display = []
    correct_letters = []
    incorrect = []
    chances = 0
    hangman_values = ['O', '/', '|', '\\', '|', '/', '\\']
    show_hangman_values = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
    for char in word:
        if char.isalpha():
            word_display.append('_')
            correct_letters.append(char.upper())
        else:
            word_display.append(char)

    while True:
        clear()
        print_hangman(show_hangman_values)
        print_word(word_display)
        print()    

if __name__ == "_main_":
    clear()

    topics = {1: "Football players", 2: "Rockstars", 3: "Marvel Characters"}

    dataset = { "Football players":["MO SALAH", "LIONEL MESSI", "KEVIN DE BRUYNE", "CRISTIANO RONALDO", "NGOLO KANTE",
    "KYLIAN MBAPPE", "NEYMAR", "KARIM BENZEMA" "DANI ALVES", "ZLATAN IBRAHIMOVIC"],\
    "Rockstars": ["LIAM GALLAGHER", "AXEL ROSE", "ERIC CLAPTON", "SLASH", "PAUL MCCARTNEY", "MICK JAGGER", "OZZY OSBOURNE",
    "JIMI HENDRIX", "BRUCE SPRINGSTEEN", "JOHN LENNON", "DAVID BOWIE"],
     "Marvel Characters":["CAPTAIN AMERICA", "IRON MAN", "THANOS", "HAWKEYE", "BLACK PANTHER", "BLACK WIDOW", "SPIDERMAN",
     "STARLORD", "THOR", "DOCTOR STRANGE"]
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
            choice = int(input("Enter your choice = "))
        except ValueError:
            clear()
            print("Wrong choice!! Try again")
            continue

        if choice > len(topics)+1:
            clear()
            print("No such topic!! Try again.")
            continue
        elif choice == len(topics)+1:
            print()
            print("Thank you for playing!")
            break
        
        chosen_topic = topics[choice]
        ran = random.choice(dataset[chosen_topic])
        hangman_game(word)    

    
