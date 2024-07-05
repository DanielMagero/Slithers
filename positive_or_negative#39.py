print("Check if the number is positive or negative.")
num = int(input("Input a number of your choice:"))

def integer_state(num):
    if num < 0:
        print(f" {num} is negative.")
    elif num > 0:
        print(f" {num} is positive.")
    else:
        print(f" {num} is zero")

integer_state(num)