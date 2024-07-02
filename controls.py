# program to return the grade of the student. Above 80 is A, 70 - 80 is B, then 60 - 70 is C

def grade(score):
    if score > 60:
        return "P"
    else:
        return "F"
    
print(grade(23))
print(grade(80))

