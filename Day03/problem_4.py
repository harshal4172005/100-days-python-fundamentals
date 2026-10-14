# Ask the user for a number n. Calculate and print the sum of all numbers from 1 to n.

n=int(input("Entere a number n:"))
total=0
for i in range(1,n+1):
    total=total+i
print("sum:",total)