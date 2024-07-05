print("This program shows a right angled triangle using numbers 0-9")

def num_nest(p):
    for i in range(p):
        for j in range (i, -1, -1):
            print(j, end="")
        print()

num_nest(10)