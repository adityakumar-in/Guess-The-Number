"""
----------------------------------Number Guessing Game---------------------------------------------

This is the Number Guessing Game. In which we generate random number whenever the program runs
and we ask the user to guess the number.
We also give hints to the user to guess the number right.
We give only 5 chances to user to guess the number, when he/she fails to do then we quit the Game.

---------------------------------------------------------------------------------------------------
"""

import random

class guess_the_number :
    def main():
        rand = random.randint(1, 100)
        inp = int(input("Guess The Number: "))
        for i in range(0, 10):    
            if inp > rand :
                print("Too High, ")
            elif inp < rand :
                print("Too Low, ")
            else :
                print("Congratulations! You guessed it Perfect")
            if inp != rand :
                inp = int(input("Guess Again: "))
            if i==4 and rand!=inp :
                print("Sorry, You Lost the game")
                break
        
    
    if __name__ == '__main__' :
        main()