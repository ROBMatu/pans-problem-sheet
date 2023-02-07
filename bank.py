# bank.py
# Author Robert O'Brien-Monk
# Take in 2 values of money in cents, add together and return in formatted reply

#prompt user
name = input("Enter your name:")
print(f"Hello {name}\nWelcome to Centbank")

cent1 = int(input("Enter first lodgement in cents:"))
cent2 = int(input("Enter second lodgement in cents:"))

#add the two ammounts
sum = (cent1 + cent2)/100

#return sum to user
print(f"The total sum in your account is: €{sum:.2f}")
