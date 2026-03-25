Facial_Features = ["Hair colour", "Skin Colour", "Facial Hair", "Hair Length", "Eye Colour"]
Accessories = []

selection = False
while selection == False:
    Choice = input("What features would you like to ask about (1) facial features or (2) accessories")
    if Choice == "1":
        selection = True
        Choice = int(input("what features about the face would you like to ask about?\n(1) Hair colour\n(2) Skin Colour\n(3) Facial Hair\n(4) Hair Length\n(5) Eye Colour\n"))
        if Facial_Features[Choice-1] in Facial_Features:
            print(f"You have selected {Facial_Features[Choice-1]}")
            if Facial_Features[Choice-1] == Facial_Features[0]:
                Choice = int(input("What Hair colour do you think they have?\n(1) Blonde\n(2) Brown\n(3) Black\n(4) Ginger\n(5) Grey\n(6) Purple\n(7) Pink\n"))
        else: 
            print("invalid")
    elif Choice == "2":
        selection = True
        print("oy")
    else:
        selection = False
        print("invalid")