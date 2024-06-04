#6. Exploring Logical Operations and Precedence
#Task 1: Validating Calculations
calculate = 5 * 4 + 7
p_calculate = 5 * (4 + 7)

if calculate == p_calculate:
    print("same answer")
else:
    print("not the same answer")

#Task 2: Mix and Match
result = (5 + 3) > 7 or (10 - 2) == 8
#I predict reult is boolean and will print out True or False
print(result)