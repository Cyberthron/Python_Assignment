# Assuming that we have some email addresses in the &quot;username@companyname.com&quot;
# format, write a program to print the company name of a given email address. Both user
# names and company names are composed of letters only.

import re       # re used for regular expression
emailAddress = input("enter the maillid :-  ")  #take the input
path = "(\w+)@(\w+)\.(com)"     # id path(we can give any thing)
r2 = re.match(path,emailAddress)    # matching the path
print (r2.group(2))         # take the second component means it take after @ and before the .com string