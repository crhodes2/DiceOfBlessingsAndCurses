import random
min = 1
max = 6
dice = random.randint(1, 6)
dice2 = random.randint(1, 6)

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print "Rolling the dices..."
    print "The values are...."
    print dice
    print dice2

    if(dice + dice2 == 6):
        print("You rolled a 6! You have been cursed!")
    elif(dice + dice2 == 7):
        print("You rolled a 7! You have been blessed with money")
    else:
        print("You don't have any blessings")

roll_again = raw_input("Roll the dices again?")