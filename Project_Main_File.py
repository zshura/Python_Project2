#ZShura_Project1

#Code was created with revision help from Per Van Dyke

#Trivia game with questions about Hampshire College

#Sets modifiers for difficulty in startup function
global easy_modifier
easy_modifier = 10
global medium_modifier
medium_modifier = 5
global hard_modifier
hard_modifier = 1

#Questions for trivia quiz. It is called into use by the startup function below.

def questions():
    print("Thank you for choosing your level. Please enjoy this trivia game!")
    print()
    score = 0

    #First the question is asked and a response is requested
    q1 = input("1. What year was Hampshire College opened? ")
    #The input answer is turned all to lowercase
    q1 = q1.lower()
    #While the inputted answer is not the correct answer
    while q1 != "1970":
        #Request another input and decrease the score equal to half the score_modifier * 1
        q1 = input("Incorrect, please try again: ")
        q1 = q1.lower()
        score -= 1 * score_modifier / 2
        #When the inputted answer is the correct answer
    else:
        #Add to the score equal to the score_modifier
        score += 1 * score_modifier
        #Print correct and move onto the next question
        print("Correct!")
        print()

    #Repeat the same pattern as above
    q2 = input("2. Is Hampshire College a private or public school? ")
    q2 = q2.lower()
    while q2 != "private":
        q2 = input("Incorrect, please try again: ")
        q2 = q2.lower()
        score -= 1 * score_modifier / 2
    else:
        score += 1 * score_modifier
        print("Correct!")
        print()

        
    q3 = input("3. What is the unique speed limit of Hampshire College campus roads? ")
    q3 = q3.lower()
    while q3 !="17":
        q3 = input("Incorrect, please try again: ")
        q3 = q3.lower()
        score -= 1 * score_modifier / 2
    else:
        score += 1 * score_modifier
        print("Correct!")
        print()

        
    q4 = input('4. What is the "unnoficial" mascot of Hampshire College? ')
    q4 = q4.lower()
    while q4 not in ("frog", "bullfrog", "bull frog"):
        q4 = input("Incorrect, please try again: ")
        q4 = q4.lower()
        score -= 1 * score_modifier / 2
    else:
        score += 1 * score_modifier
        print("Correct!")
        print()


    q5 = input("5. Is Hampshire College a small, medium, or large college? ")
    q5 = q5.lower()
    while q5 != "small":
        q5 = input("Incorrect, please try again: ")
        q5 = q5.lower()
    else:
        score += 1
        print("Correct!")
        print()
        EndGame(score)



#The EndGame function closes out the program and provides the player with their final score.
#They are also asked if they would like to play again.
def EndGame(score):
    print("Good job! You have completed the trivia.")
    print()
    print("Your final score is ", score)
    print()
    replay = input("Would you like to play again? ")
    replay = replay.lower()
    print()
    if replay == "yes":
        return startup()
    if replay == "no":
        print("Thanks for playing!")


#The startup function starts off the game and prompts the player to choose which difficulty they would like to use.
    
def startup():
    print("Hello! Welcome to The Hampshire College Trivia Game!")
    print()
    print("There are three levels of difficulty to this game.")
    print("The level determines the score modifier.")
    print()
    difficulty = input("Please choose easy, medium, or hard: ")
    difficulty = difficulty.lower()
    global score_modifier

    #According to the difficulty the player chooses, the score_modifier changes.
         
    if difficulty == "easy":
        score_modifier = easy_modifier
        return questions()
    
    elif difficulty == "medium":
        score_modifier = medium_modifier
        return questions()
    
    elif difficulty == "hard":
        score_modifier = hard_modifier
        return questions()
    else:
        print("Error: mode not inputed properly. Reload launching.")
        startup()


startup()

## EXTRA IDEAS ##
#DONE - Once mode has been played through, display score
#DONE - Ask if want to play again?
#Leaderboard?
#Second round of questions?
