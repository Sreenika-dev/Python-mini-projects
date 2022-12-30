import random 
import time

roll_the_dice = "yes"
while roll_the_dice =="yes":
    dice1 = random.randint(1,6)
    print(f"dice1: {dice1}")
    dice2 = random.randint(1,6)
    print(f"dice2: {dice2}")
    roll_the_dice = input("Want to roll the dice again?(yes/no) ")
    if roll_the_dice=="no":
        break
    else:
     print("Dice rolling....")
     time.sleep(5)