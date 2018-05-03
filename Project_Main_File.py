#ZShura_Project2

# import from Project_Questions.py

def Start_up():
    """The Start_up function begins the program by asking what round of questions you would like to take."""

    print("Hello! Welcome to The Hampshire College Trivia Game!")
    print("There are three sets of questions you can chose from: Anagrams, Quick Facts, and Presidents.")



def End_Game(score):
    """The End_Game function will close out the program once it has been run through after
    providing the player with their final score. It also offers a chance to replay the game."""
    
    print("Good job! You have completed the trivia.\nYour final score is ", score)
    print()
    replay.lower() = input("Would you like to play again? ")
    print()
    if replay == "yes":
        return startup()
    if replay == "no":
        print("Thanks for playing!")


Start_up()
