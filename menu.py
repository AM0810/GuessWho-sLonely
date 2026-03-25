Facial_Features = ["Hair colour", "Skin Colour", "Facial Hair", "Hair Length", "Eye Colour"]
Hair_Colour = ["Blonde", "Brown", "Black", "Ginger", "Grey", "Purple", "Pink"]
Skin_Colour = ["White", "Black"]
Facial_Hair = ["Yes", "No"]
Hair_Length = ["Short", "Medium", "Long"]
Eye_Colour = ["Blue", "Green", "Brown", "Black", "Purple"]
Accessories = ["Earrings", "Glasses", "Hat"]
Earrings = ["Yes", "No"]
Glasses = ["Yes", "No"]
Hat = ["Yes", "No"]

selection = False
while selection == False:
    Choice = input("What features would you like to ask about (1) facial features or (2) accessories\n")
    if Choice == "1":
        selection = True
        Choice = int(input("What features about the face would you like to ask about?\n(1) Hair Colour\n(2) Skin Colour\n(3) Facial Hair\n(4) Hair Length\n(5) Eye Colour\n"))
        if Facial_Features[Choice-1] == Facial_Features[0]:
                print(f"You have selected {Facial_Features[Choice-1]}")
                Choice  = input("What hair colour do you think they have?\n(1) Blonde\n(2) Brown\n(3) Black\n(4) Ginger\n(5) Grey\n(6) Purple\n(7) Pink")
        elif Facial_Features[Choice-1] == Facial_Features[1]:
                print(f"You have selected {Facial_Features[Choice-1]}")
                Choice  = input("What skin colour do you think they have?\n(1) White\n(2) Black\n")
        elif Facial_Features[Choice-1] == Facial_Features[2]:
                print(f"You have selected {Facial_Features[Choice-1]}")
                Choice  = input("Do you think they have facial hair?\n(1) Yes\n(2) No\n")
        elif Facial_Features[Choice-1] == Facial_Features[3]:
                print(f"You have selected {Facial_Features[Choice-1]}")
                Choice  = input("What hair length do you think they have?\n(1) Short\n(2) Medium\n(3) Long\n")
        elif Facial_Features[Choice-1] == Facial_Features[4]:
                print(f"You have selected {Facial_Features[Choice-1]}")
                Choice  = input("What eye colour do you think they have?\n(1) Blue\n(2) Green\n(3) Brown\n(4) Black\n(5) Purple\n")
        else:
            print("invalid")
    elif Choice == "2":
        selection = True
        Choice = int(input("What accessories would you like to ask about?\n(1) Earrings\n(2) Glasses\n(3) Hat\n"))
        if Accessories[Choice-1] == Accessories[0]:
                print(f"You have selected {Accessories[Choice-1]}")
                Choice  = input("Do you think they have earrings?\n(1) Yes\n(2) No\n")
        elif Accessories[Choice-1] == Accessories[1]:
                print(f"You have selected {Accessories[Choice-1]}")
                Choice  = input("Do you think they have glasses?\n(1) Yes\n(2) No\n")
        elif Accessories[Choice-1] == Accessories[2]:
                print(f"You have selected {Accessories[Choice-1]}")
                Choice  = input("Do you think they have a hat?\n(1) Yes\n(2) No\n")
        else:
            print("invalid")
    else:
        selection = False
        print("invalid")