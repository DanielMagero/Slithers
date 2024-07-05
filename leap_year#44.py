print("Determining if a year is a leap year. \nEnter a year of your choice below:")

yr = int(input( ))

def lp_yr(yr):
    if yr % 4 == 0 and yr % 100 != 0 or (yr % 400 == 0):
        print(f"{yr} is a leap year.")
    else:
        print(f"{yr} is not a leap year.")
    
lp_yr(yr)