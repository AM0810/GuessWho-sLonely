import pandas as pd
from random import randint
charactersdf = pd.read_csv(open('Names.csv', "r"))

# Main menu if the computer is the one guessing the player's character
def ComputerGuesserMenu():
    # storing lists of possible values for each attribute
    HairLengths = ["long", "medium", "short"]
    HairColours = ["blonde", "brown", "black", "ginger", "silver", "pink", "purple"]

    # handles the "Does your character have (x) length hair?" question
    def HairLengthQuestionFunction():
        
        def HairLengthRandomiser():
            # If the length of the list is bigger than 1
            if len(HairLengths) > 1:
                # Generate a random number between 0 and the length of the list minus one (to prevent an index error as indexes start at 0)
                RandomHairLength = randint(0, len(HairLengths)-1)
                # HairLength stores the randomised hair length ...
                HairLength = HairLengths[RandomHairLength]
                # ... then removes that value from the list, so the question can't be repeated.
                HairLengths.remove(HairLength)
            # If the length of the list is smaller or equal to 1
            else:
                # The hair length *must* be the only one remaining in the list, as the others have been ruled out.
                HairLength = HairLengths[0]
            return HairLength
        HairLength = HairLengthRandomiser()
        Question = input(f"Does your character have {HairLength} length hair? (yes/no): ").lower()
        return Question

    def HairColourQuestionFunction():
        RandomHairColour = randint(0, len(HairColours))
        Question = input(f"Does your character have {HairColours[RandomHairColour]} coloured hair? (yes/no): ").lower()
        HairColours.remove(HairColours[RandomHairColour])
        return Question


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
        # handles unexpected inputs
        else:
            print("Invalid input! Try again.")

    while True:
        HairLengthQuestion = HairLengthQuestionFunction()

    # HairColourQuestion = HairColourQuestionFunction()

ComputerGuesserMenu()