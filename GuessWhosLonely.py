import pandas as pd
from random import randint
charactersdf = pd.read_csv(open('Names.csv', "r"))
possiblecharactersdf = charactersdf
charactersdf["HairLength"] = charactersdf["HairLength"].str.lower()
charactersdf["HairColour"] = charactersdf["HairColour"].str.lower()
charactersdf["SkinColour"] = charactersdf["SkinColour"].str.lower()
charactersdf["HasEarrings"] = charactersdf["HasEarrings"].str.lower()
charactersdf["HasGlasses"] = charactersdf["HasGlasses"].str.lower()
charactersdf["HasFacialHair"] = charactersdf["HasFacialHair"].str.lower()
charactersdf["HasHat"] = charactersdf["HasHat"].str.lower()
charactersdf["EyeColour"] = charactersdf["EyeColour"].str.lower()
possiblecharactersdf["HairLength"] = charactersdf["HairLength"].str.lower()
possiblecharactersdf["HairColour"] = charactersdf["HairColour"].str.lower()
possiblecharactersdf["SkinColour"] = charactersdf["SkinColour"].str.lower()
possiblecharactersdf["HasEarrings"] = charactersdf["HasEarrings"].str.lower()
possiblecharactersdf["HasGlasses"] = charactersdf["HasGlasses"].str.lower()
possiblecharactersdf["HasFacialHair"] = charactersdf["HasFacialHair"].str.lower()
possiblecharactersdf["HasHat"] = charactersdf["HasHat"].str.lower()
possiblecharactersdf["EyeColour"] = charactersdf["EyeColour"].str.lower()

# Main menu if the computer is the one guessing the player's character
def ComputerGuesserMenu():

    Questions = ["1", "2", "3", "4", "5", "6", "7", "8"]
    def QuestionRandomiser():
        if len(Questions) > 1:
            RandomQuestion = randint(0, len(Questions)-1)
            ChosenQuestion = Questions[RandomQuestion]
            Questions.remove(ChosenQuestion)
        else:
            ChosenQuestion = Questions[0]
        return ChosenQuestion

    # storing lists of possible values for each attribute
    HairLengths = ["long", "medium", "short"]
    HairColours = ["blonde", "brown", "black", "ginger", "silver", "pink", "purple"]
    SkinColours = ["white", "black", "brown"]
    EyeColours = ["black", "green", "brown", "blue", "purple"]


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
        return [Question, HairLength]

    # handles the "Does your character have (x) colour hair?" question
    def HairColourQuestionFunction():
        def HairColourRandomiser():
            if len(HairColours) > 1:
                RandomHairColour = randint(0, len(HairColours)-1)
                HairColour = HairColours[RandomHairColour]
                HairColours.remove(HairColour)
            else:
                HairColour = HairColours[0]
            return HairColour
        HairColour = HairColourRandomiser()
        Question = input(f"Does your character have {HairColour} colour hair? (yes/no): ").lower()
        return [Question, HairColour]

    # handles the "Does your character have (x) skin?" question
    def SkinColourQuestionFunction():
        def SkinColourRandomiser():
            if len(SkinColours) > 1:
                RandomSkinColour = randint(0, len(SkinColours)-1)
                SkinColour = SkinColours[RandomSkinColour]
                SkinColours.remove(SkinColour)
            else:
                SkinColour = SkinColours[0]
            return SkinColour
        SkinColour = SkinColourRandomiser()
        Question = input(f"Does your character have {SkinColour} skin? (yes/no): ").lower()
        return [Question, SkinColour]

    # handles the "Does your character have (x) eyes?" question    
    def EyeColourQuestionFunction():
        def EyeColourRandomiser():
            if len(EyeColours) > 1:
                RandomEyeColour = randint(0, len(EyeColours)-1)
                EyeColour = EyeColours[RandomEyeColour]
                EyeColours.remove(EyeColour)
            else:
                EyeColour = EyeColours[0]
            return EyeColour
        EyeColour = EyeColourRandomiser()
        Question = input(f"Does your character have {EyeColour} eyes? (yes/no): ").lower()
        return [Question, EyeColour]

    # all of these handle the "Does your character wear/have (x)?" questions for earrings, glasses, facial hair and hats
    def HasEarringsQuestionFunction():
        Question = input("Does your character wear earrings? (yes/no): ").lower()
        return Question

    def HasGlassesQuestionFunction():
        Question = input("Does your character wear glasses? (yes/no): ").lower()
        return Question
    
    def HasFacialHairQuestionFunction():
        Question = input("Does your character have facial hair? (yes/no): ").lower()
        return Question
    
    def HasHatQuestionFunction():
        Question = input("Does your character wear a hat? (yes/no): ").lower()
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
    
    CharacterFound = False
    while CharacterFound == False:
        ChosenQuestion = QuestionRandomiser()
    if ChosenQuestion == "1":
        while True:
            ListHairLength = HairLengthQuestionFunction()
            if ListHairLength[0] == "yes" or ListHairLength[0] == "y":
                HairLength = ListHairLength[1]
                possiblecharactersdf = possiblecharactersdf[possiblecharactersdf["HairLength"] == HairLength]
                if len(possiblecharactersdf.index) == 1:
                    CharacterFound = True
                break
            if ListHairLength[0] == "no" or ListHairLength[0] == "n":
                continue
            else:
                print("Invalid input! Please type yes or no")
                continue
    elif ChosenQuestion == "2":
        while True:
            ListHairColour = HairColourQuestionFunction()
            if ListHairColour[0] == "yes" or ListHairColour[0] == "y":
                HairColour = ListHairColour[1]
                possiblecharactersdf = possiblecharactersdf[possiblecharactersdf["HairColour"] == HairColour]
                if len(possiblecharactersdf.index) == 1:
                    CharacterFound = True
                break
            if ListHairColour[0] == "no" or ListHairColour[0] == "n":
                continue
            else:
                print("Invalid input! Please type yes or no")
                continue
    elif ChosenQuestion == "3":
        while True:
            ListSkinColour = SkinColourQuestionFunction()
            if ListSkinColour[0] == "yes" or ListSkinColour[0] == "y":
                SkinColour = ListSkinColour[1]
                possiblecharactersdf = possiblecharactersdf[possiblecharactersdf["SkinColour"] == SkinColour]
                if len(possiblecharactersdf.index) == 1:
                    CharacterFound = True
                break
            if ListSkinColour[0] == "no" or ListSkinColour[0] == "n":
                continue
            else:
                print("Invalid input! Please type yes or no")
                continue
    elif ChosenQuestion == "4":
        while True:
            ListEyeColour = EyeColourQuestionFunction()
            if ListEyeColour[0] == "yes" or ListEyeColour[0] == "y":
                EyeColour = ListEyeColour[1]
                possiblecharactersdf = possiblecharactersdf[possiblecharactersdf["EyeColour"] == EyeColour]
                if len(possiblecharactersdf.index) == 1:
                    CharacterFound = True
                break
            if ListEyeColour[0] == "no" or ListEyeColour[0] == "n":
                continue
            else:
                print("Invalid input! Please type yes or no")
                continue

    elif ChosenQuestion == "5":
        HasEarrings = HasEarringsQuestionFunction()
        if HasEarrings == "yes" or HasEarrings == "y":
            possiblecharactersdf = possiblecharactersdf[possiblecharactersdf["HasEarrings"] == HasEarrings]
            print(possiblecharactersdf)
            if len(possiblecharactersdf.index) == 1:
                CharacterFound = True
        if HasEarrings == "no" or HasEarrings == "n":
            possiblecharactersdf = possiblecharactersdf[possiblecharactersdf["HasEarrings"] != HasEarrings]
            print(possiblecharactersdf)

    elif ChosenQuestion == "6":
        Glasses = HasGlassesQuestionFunction()
    elif ChosenQuestion == "7":
        FacialHair = HasFacialHairQuestionFunction()
    elif ChosenQuestion == "8":
        Hat = HasHatQuestionFunction()
    
    print(possiblecharactersdf)

ComputerGuesserMenu()