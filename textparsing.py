#times I have regretting agreeing to do this counter: 2

InputText = input("Input text here!!: ").lower().split()

Hello = False
Bye = False

for word in InputText:
    if word == "hello" or word == "hi":
        Hello = True
    elif word == "bye" or word == "goodbye":
        Bye = True

if Hello == True:
    print("hi! :D")

if Bye == True:
    print("goodbye! :D")

# okay I think I'm done here for the night