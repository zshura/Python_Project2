#ZShura_Project2

# from Project_Questions import Anagrams, Quick_facts, Presidents

# Checklist:
# - Create all the doc strings
# - Finish Presidents

def Startup():
    """The Start_up function begins the program by asking what round of questions you would like to take."""

    print("Hello! Welcome to The Hampshire College Trivia Game!\n")
    print("There are three sets of questions you can chose from: Anagrams, Quick Facts, and Presidents.")
    level = input("What set of questions would you like to play? ")
    level = level.lower()
    print("Thank you for choosing", level, "!")
    
    if level == "anagrams":
        from Project_Questions import Anagrams
        d = Anagrams()
        return d, Game(d)
    if level == "quick facts":
        from Project_Questions import Quick_facts
        d = Quick_facts()
        return d, Game(d)
    if level == "presidents":
        from Project_Questions import Presidents
        d = Presidents()
        return d, Game(d)
    else:
        print("Incorrect input. Please try again.")
           

def Game(d):
    score = 0
    for key, value in d.items():
        answer = input(key)
        answer = answer.lower()
        while answer != value:
            answer = input("whoopsie")
            score -= 1
        else:
             print("Correct!")
             score += 1
    print(score)
        
    
    


##def End_Game(score):
##    """The End_Game function will close out the program once it has been run through after
##    providing the player with their final score. It also offers a chance to replay the game."""
##    
##    print("Good job! You have completed the trivia.\nYour final score is ", score)
##    print()
##    replay = input("Would you like to play again? ")
##    print()
##    if replay == "yes":
##        return startup()
##    if replay == "no":
##        print("Thanks for playing!")


d = Startup()
