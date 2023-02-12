# accounts.py
# Author: Robert O'Brien-Monk
# Bank 10 digit account number as string inputted
# then all but last 4 digits replaced with an x 

# To deal with account numbers of any length. 
# A for loop may be used to go through a substring minus the last 4 digits 
# and replace each character of the substring with an x. 
# Then join it with another another substring contaning the last 4 digits of the account number.
# Comment out line 13,15,16,22 . Uncomment line 12,18,19,20,23  for this version.

#acc_num = input("Please enter your account number: ")
account_number = input("Please enter your 10 digit account number: ")

last_four = account_number[-4:]
security_X = account_number.replace(account_number[0:7], "XXXXXX").strip(account_number[-4:])

#format_acc = acc_num.strip(acc_num[-4:])
#for digit in format_acc:
#    format_acc = format_acc.replace(digit, "X")
    
print(security_X + last_four)
#print(format_acc + last_four)
