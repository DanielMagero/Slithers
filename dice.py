import random

tries = 0


def roll_dice_until_doubles():
    global tries

    doubles = False

    while not doubles:
        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)

        print(f"Rolled {roll1} and {roll2}")
        
        tries += 1

        if roll1 == roll2:
            print(f"Doubles in {tries} tries!")
            doubles = True

roll_dice_until_doubles()