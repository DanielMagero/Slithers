print("Welcome to Bobic's Restaurant")

print("Menu")
print("1. Chicken Biryani")
print("2. Mutton Biryani")
print("3. Veg. Biryani")
print("4. Chicken Fried Rice")
print("5. Rolex")
print("6. Lusaniya")
print("7. Pork ribs")
print("8. Sushi")

order = input("What would you like to order? Enter the choice (1-8): ")

if order == "1":
    print("You have chosen Chicken Biryani. Your bill is 34,000 UGX.")
elif order == "2":
    print("You have chosen Mutton Biryani. Yout bill is 33,000 UGX.")
elif order == "3":
    print("You have chosen Veg. Biryani. Your bill is 36,000 UGX.")
elif order == "4":
    print("You have chosen Chicken Fried Rice. Your bill is 24,000 UGX." )
elif order == "5":
    print("You have chosen Rolex. Your bill is 10,000 UGX." )
elif order == "6":
    print("You have chosen Lusaniya. Your bill is 55,000 UGX." )
elif order == "7":
    print("You have chosen Pork Ribs. Your bill is 38,000 UGX." )
else:
    print("You have chosen Sushi. Your bill is 36,000 UGX.")
