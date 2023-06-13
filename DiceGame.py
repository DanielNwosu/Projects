import random

rolls = 5
chips = 100

print("You have five rolls to make your point\n")
print("Your bet cannot exceed the amount you have left in your bank\n")
print("You have 100 chips in your bank\n")

bet = int(input("Place your bet: "))
points = int(input("What is your points: "))

i = 1
win = 0

while(rolls > 0):
    print("You have "+str(rolls)+" rolls to make your point\n")
    print("Rolling the dice\n")
    print("Roll number "+str(i)+" of 5")
    print("The values are: ")
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print(dice1)
    print(dice2)
    print("\nYou rolled a "+str(dice1+dice2))
    print("Your point is "+str(points))
    if(dice1 + dice2 != points):
        print("Sorry, you didn't make your point")
        i += 1
        rolls -= 1
    else:
        print("Congrats you made your point!")
        win = 1
        break
if(win):
    print("Your bet is doubled\n")
    print("The total value of your chips in bank: "+str(chips+bet*2))
else:
    print("Your amount will be decreased by your bet")
    print("The value of your remaining chips is: "+str(chips-bet))