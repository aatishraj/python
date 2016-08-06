'''
from passwd file Find out all the
users that have the same UID.
'''

import collections

file = open('/Users/aatishk/PycharmProjects/python_files/passwd')
pass_file = file.read().split()

pass_dict = collections.defaultdict(list)

for line in pass_file:
    user = line.split(':')[0]
    uid = line.split(':')[2]
    pass_dict[uid].append(user)

for k,v in pass_dict.items():
    if len(v) > 1:
        print "Users" , ", ".join(v) , "have duplicate uid:" , k