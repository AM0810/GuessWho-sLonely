import pandas as pd
from random import randint
charactersdf = pd.read_csv(open('Names.csv', "r"))

def ComputerGuesserMenu():
    HairLengths = ["Long", "Medium", "Short"]
    HairColours = ["Blonde", "Brown", "Black", "Ginger", "Silver", "Pink", "Purple"]

    def HairLengthQuestionFunction():
        RandomHairLength = randint(0, len(HairLengths))
        HairLengthQuestion = input(f"Does your character have {HairLengths[RandomHairLength]} hair? (yes/no): ").lower()
        HairLengths.remove(HairLengths[RandomHairLength])
        return HairLengthQuestion

    def HairColourQuestionFunction():
        RandomHairLength = randint(0, len(HairLengths))
        HairLengthQuestion = input(f"Does your character have {HairLengths[RandomHairLength]} hair? (yes/no): ").lower()
        HairLengths.remove(HairLengths[RandomHairLength])
        return HairLengthQuestion


    print("The computer is now the guesser.")
    print("--------------------------------")
    print("Think of a character!")
    # asks the user if they have thought of a character yet, to start the game
    while True:
        response = input("Have you thought of a character? (yes/no): ").lower()
        if response == "y" or response == "yes":
            print("Okay! Let's play Guess Who's Lonely!")
            print("--------------------------------")
            break
        if response == "n" or response == "no":
            print ("Well, you better think of somebody!")
        else:
            print("Invalid input! Try again.")

