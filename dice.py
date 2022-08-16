import random
from time import sleep
import sys

def game(): 
    while True: 
        dice = [1,2,3,4,5,6]
        dice_1_answer = random.choice(dice)
        sleep(2.0)
        print(f"Your first dice is equal to {dice_1_answer}\n")
        sleep(2.0)
        dice_2_answer = random.choice(dice)
        print(f"Your second dice is equal to {dice_2_answer}\n")  
        sleep(2.0)
        result = dice_1_answer + dice_2_answer
        print(f"Your dice roll is equal to {result}\n")
        comp_dice_1_answer = random.choice(dice)
        sleep(2.0)
        print(f"Opponent first dice is equal to {comp_dice_1_answer}\n")
        sleep(2.0)
        comp_dice_2_answer = random.choice(dice)
        print(f"Opponent second dice is equal to {comp_dice_2_answer}\n")  
        sleep(2.0)
        comp_result = comp_dice_1_answer + comp_dice_2_answer
        print(f"Opponent dice roll is equal to {comp_result}\n")
        sleep(2.0)
        if comp_result > result:
            print("YOU LOSE\n")
            break
        elif comp_result < result:
            print("YOU WIN\n")
        else:
            print("TIE\n")
        break 
        
def replay():
    while True:
        replay = input("Would you like to play again? Yes or No: ").upper()
        if replay == "YES":
            game()
        elif replay == "NO":
            break 
        
    
game()
sleep(2.0)
replay()
    