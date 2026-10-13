'''
Problem 5 (slightly harder)

Ask for marks (out of 100). Print the grade:

90+ → A
75–89 → B
50–74 → C
below 50 → Fail 
'''

marks=int(input("Enter you marks :"))
if marks>=90:
    print("A")
elif marks>=75 and marks<=89:
    print("B")
elif marks>=50 and marks<=74:
    print("C")
else:
    print("FAIL")