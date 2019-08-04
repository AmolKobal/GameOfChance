import random

def cho_han(gauss, bet_amount):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        dice_total = dice1 + dice2
        outcome = ""

        if(dice_total % 2 == 0):
            outcome = "EVEN"
        else:
            outcome = "ODD"

        if(gauss.upper() == outcome):
            return bet_amount
        return 0
