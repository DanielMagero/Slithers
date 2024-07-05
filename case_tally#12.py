print("Enter a word with varying number of uppercase and lowercase letters: ")

word = input()

upper = 0
lower = 0

for char in word:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1

print(f" The number of upper case letters is {upper}. \n The number of lower case letters is {lower}.")