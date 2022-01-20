import os
import random

def clear():
    os.system("cls")

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

    
