print("Get your mulptiplication table.")

num = int(input("Enter any number: "))

num2 = 1

while num2 < 11:
    ans = num * num2
    print(f"{num} x {num2} = {ans}")

    num2 += 1
