Facial_Features = ["Hair colour", "Skin Colour", "Facial Hair", "Hair Length", "Eye Colour"]
Hair_Colour = ["Blonde", "Brown", "Black", "Ginger", "Grey", "Purple", "Pink"]
Skin_Colour = ["White", "Black"]
Facial_Hair = ["Yes", "No"]
Hair_Length = ["Short", "Medium", "Long"]
Eye_Colour = ["Blue", "Green", "Brown", "Black", "Purple"]
Accessories = []

selection = False
while selection == False:
    Choice = input("What features would you like to ask about (1) facial features or (2) accessories\n")
    if Choice == "1":
        selection = True
        Choice = int(input("what features about the face would you like to ask about?\n(1) Hair colour\n(2) Skin Colour\n(3) Facial Hair\n(4) Hair Length\n(5) Eye Colour\n"))
        if Facial_Features[Choice-1] in Facial_Features:
            print(f"You have selected {Facial_Features[Choice-1]}")
            
        elif Facial_Features[Choice-1] == Facial_Features[0]:
                print(f"You have selected {Facial_Features[Choice-1]}")
        elif Facial_Features[Choice-1] == Facial_Features[1]:
                print(f"You have selected {Facial_Features[Choice-1]}")
        elif Facial_Features[Choice-1] == Facial_Features[2]:
                print(f"You have selected {Facial_Features[Choice-1]}")
        elif Facial_Features[Choice-1] == Facial_Features[3]:
                print(f"You have selected {Facial_Features[Choice-1]}")
        elif Facial_Features[Choice-1] == Facial_Features[4]:
                print(f"You have selected {Facial_Features[Choice-1]}")
        else:
            print("invalid")
    elif Choice == "2":
        selection = True
        print("oy")
    else:
        selection = False
        print("invalid")