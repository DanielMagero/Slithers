import time

def countdown(seconds):
    while seconds > 0:
        print('T-Minus', seconds)
        seconds -= 1
        time.sleep(1)

    print("Blastoff!!")

print("Enter the duration of your plank in seconds.")
seconds = int(input())

countdown(seconds)