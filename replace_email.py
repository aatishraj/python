'''
replace the user_name part of the email with REMOVED
example: aatish@yahoo.com  ==> REMOVED@yahoo.com
'''

import re

# Read contents from file as a single string
file = open('/Users/aatishk/PycharmProjects/python_files/mbox1.txt', 'r')
text = file.read()
file.close()

# Use RegEx to find and replace
text = re.sub('\S+@', 'REMOVED@', text)

# Write contents to file.
file = open('/Users/aatishk/PycharmProjects/python_files/mbox1.txt', 'w')
file.write(text)
file.close()