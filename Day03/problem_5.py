'''
Ask the user to enter 5 numbers (one by one). Store them in a list.

Then print:

The full list
The maximum number in the list
'''

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))
d=int(input("Enter 4th number: "))
e=int(input("Enter 5th number: "))

numbers=[a,b,c,d,e]
print(numbers)
print(max(numbers))