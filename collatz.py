# collatz.py
# Author: Robert O'Brien-Monk
# Ask for input of a positive number then
# output the collatz conjucture calculation results

positive_integer = int(input("Please enter a positive integer: "))

# Store numbers from calculations in while loop
num_list = []

# Add inital input to list
num_list.append(positive_integer)

# Collatz conjucture calculation, Even divide by 2, Odd multiply by 3 and add 1
while positive_integer != 1:
    if positive_integer %2 == 0:
        positive_integer = positive_integer // 2
        num_list.append(positive_integer)
    else:
        positive_integer = (positive_integer * 3) + 1
        num_list.append(positive_integer)

# Prints numbers from list on same line with no commas
for num in num_list:
    print(num, end=" ")
