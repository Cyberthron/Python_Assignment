# Binary Search

pos=-1
def binarysearch(a,s):
    f=0
    l=n-1
    while f<=l :
        mid=(f+l)//2
        if a[mid]==s :
            globals()['pos']=mid
            return True
        else:
            if a[mid]<= s:
                f=mid
            else:
                l=mid

a = []
n = int(input('no. of element you want'))
for j in range(0,n):
    element=int(input('enter the element'))
    a.append(element)
a.sort();
s=int(input('what element you want to search'))

print(a)
if binarysearch(a,s):
    print('Index Position of the search element',pos)
else:
    print('Not found')