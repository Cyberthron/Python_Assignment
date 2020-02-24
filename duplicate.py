#With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list
# after removing all duplicate values with original order reserved.
# Hint: Use set() to store a number of values without duplicates.


def removeDuplicate( list ):   #Create a function removeDuplicate
    new_list=[]
    seen = set()            #set() is used for convert any iteration to distinct values and sort them
    for item in list:
        if item not in seen:
            seen.add( item )
            new_list.append(item)       #append function is used to added the values

    return new_list

list=[12,24,35,24,88,120,155,88,120,155]
print(removeDuplicate(list))