import random  #Imports the random functions.

min = 1 #Minimum number
max = 6 #Maximum number

def roll():  #Function called roll Created

    # UserInput for whether to roll the dice or not
    roll_again = input("Would you like to roll again? (Yes or No)")

    if roll_again == "yes" or roll_again == "y":
        print ("Rolling the dice...")
        print ("You rolled: ")
        print (random.randint(min, max))
        roll()
    else:
        print("Thank you, goodbye!")


print("\n------------DICE ROLLING SIMULATOR---------------\n")
roll()
