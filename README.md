# **pans-problem-sheet**
##### Author : Robert O'Brien-Monk

---

## Synopsis
This repository pans-problem-sheet contains the weekly tasks given in the Programming and Scripting module 
on the Higher Diploma in Science - Computing (Data Analytics) course from ATU Galway-Mayo.

## Weekly tasks
---

### Contents

1. helloworld.py
2. bank.py
3. accounts.py
4. collatz.py
5. weekday.py
6. squareRoot.py
7. es.py
8. plottask.py

---
### **helloworld.py**

This is a basic program that prints out the string 'Hello World!' to the user.

---

### **bank.py**
This program does the following: 

Prompts the user for name and then greets them.
Then two money amounts in cents are inputted by the user.
which are then added together and divided by 100 to a floating point number that could be formatted to represent euro.
The Sum is then formatted with a € euro sign and decimal point and rounded to 2 decimal places after the point.

---

### **accounts.py**
This program contains two versions of the program that do the following:

**The first:**
A Bank 10 digit account number as string is inputted,
then all but the last 4 digits replaced with an x 

**The second:**
To deal with account numbers of any length. 
A for loop may be used to go through a substring minus the last 4 digits 
and replace each character of the substring with an x. 
Then join it with another another substring contaning the last 4 digits of the account number.
Comment out line 13,15,16,22  and then Uncomment line 12,18,19,20,23  for this version.

---

### **collatz.py**
This program does the following:

Asks for an input of a positive number. It then enters that number into the collatz calculations that, if Even divide by 2, Odd multiply by 3 and add 1. Then the collatz conjucture calculation results are printed out.

---

### **weekday.py**
This program does the following:

It uses the dattime module in order to output if today is a weekday or not. By getting the fullname of today and checking if its in a list of weekdays of Monday to Friday. Then outputting either "Yes, today is a weekday!" or "We are in the weekend!"

#### _references for weekday.py_
[w3schools](https://www.w3schools.com/python/python_datetime.asp)

---

### **squareRoot.py**
This program does the following:

It takes an input of positive floating-point number. Then it outputs an approximate square root of the number using newton square root formula.

#### _references for squareRoot.py_
[tutorialsinhand](https://tutorialsinhand.com/Articles/python-program-to-find-square-root-of-a-number-using-newton-square-root-formula.aspx)

[stackoverflow](https://stackoverflow.com/questions/28733759/python-square-function-using-newtons-algorithm)

---

### **es.py**
This program does the following: 

It reads in a text file and returns how many letter e's it contains. It takes the filename from an argument on the command line.

#### _references for es.py_
[geeksforgeeks](https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/)
[stackoverflow](https://stackoverflow.com/questions/7033987/get-a-file-from-cli-input)

---

### **plottask.py**
This program does the following:
It creates a histogram of a normal distribution of a 1000 values, with a mean of 5 and standard deviation of 2. And a plot of the function  h(x)=x3 in the range [0, 10]

#### _references for plottask.py_
[w3schools matplotlib labels](https://www.w3schools.com/python/matplotlib_labels.asp)
[w3schools matplotlib line](https://www.w3schools.com/python/matplotlib_line.asp)
[w3schools matplotlib grid](https://www.w3schools.com/python/matplotlib_grid.asp)
[matplotlib.org colours](https://matplotlib.org/stable/gallery/color/named_colors.html)

---

### **software used and resources**
 Visual Studio Code - version 1.74.3
 
 [medium.com readme file](https://medium.com/analytics-vidhya/how-to-create-a-readme-md-file-8fb2e8ce24e3)

