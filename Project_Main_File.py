# ZShura_Project2


def Startup():
    """The Start_up function begins the program and activates other functions as needed."""

    print("Hello! Welcome to The Hampshire College Trivia Game!\n")
    print("There are three sets of questions you can chose from: Anagrams, Quick Facts, and Presidents.")
    level = input("What set of questions would you like to play? ")
    level = level.lower()
    if level != "anagrams" or "quick facts" or "presidents":
        level = input("Set not properly chosen. Please input either Anagrams, Quick Facts, or Presidents: ")
        level = level.lower()
    if level == "anagrams" or "quick facts" or "presidents":
        print("Thank you for choosing", level, "!")
        return level, Level_choice(level)


def Level_choice(level):
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
        print("Please be aware Presidents are listed by first name and last name, but not middle initial.")
        return d, Game(d)
    else:
        print("Incorrect input. Please try again.")
        return Startup()


def Game(d):
    """Runs the questions circuit depending on which questions were selected."""
    score = 0
    for key, value in d.items():
        answer = input(key)
        answer = answer.lower()
        while answer != value:
            answer = input("Incorrect, please try again: ")
            score -= 1
        else:
            print("Correct!")
            score += 1
    return score, End_Game(score)


def End_Game(score):
    """Will close out the program once it has been run through after providing the
player with their final score. It also offers a chance to play other sections of the game."""

    print("Good job! You have completed the trivia.\nYour final score is ", score)
    print()
    replay = input("Would you like to play a different level?: ")
    replay = replay.lower()
    if replay == "yes":
        return Startup()
    if replay == "no":
        print("Thanks for playing!")


d = Startup()
