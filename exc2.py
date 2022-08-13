import random
from collections import Counter
from enum import Enum


game_lenght = 100
boxes_tupple = ("green", "orange", "violet", "gold")
boxes_prizes = (1000, 4000, 30000, 100000)
#green = 75%, orange = 20%, violet = 4%, gold = 1%


def get_box():
    selected_box = random.choices(boxes_tupple, [0.75, 0.25, 0.04, 0.01], k=100)
    print(random.choice(selected_box))


while game_lenght > 0:
    decision = input(str(("Do you want to move forvard?: (print yes or no):")))
    if(decision == 'y'):
        print("soo.. you move on!")
        get_box()

        game_lenght -= 1
    else:
        print("Game over")
        break


print("Game Over 5!")