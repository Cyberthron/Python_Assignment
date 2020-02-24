
#Implement a program dir_tree.py that takes a directory as argument and prints all the files
# in that directory recursively as a tree.
# Hint: Use os.listdir and os.path.isdir functions.

import os
spath=r"D:\python"
print(os.listdir(spath))

for root,dirs,files in os.walk(spath):

    for dir in dirs:
        print("dir ",dir)
        
    for file in files:
        print("Files ",file)


