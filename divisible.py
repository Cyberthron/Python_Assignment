#With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list
# after removing all duplicate values with original order reserved.
# Hint: Use set() to store a number of values without duplicates.


n=int(input('Enter the number :- ')) # take input
nl=[]   # create a list
for x in range(0, n):
    if (x%5==0) and (x%7==0):
        nl.append(str(x))   #values append to the list
print (','.join(nl))