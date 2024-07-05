print("We are going to get a division table of nay number. \n Enter any number of your choice:")

num = int(input())

num2 = 1

while num2 < 10:
    quo = num/num2
    num2 += 1
    print(f"{num} / {num2} = {quo}")