'''
Find the largest number in the list.
'''

myList = [-1 , 5, 2, 3, 9, 10, 7, 8, 15, 20, 13, 1, 4, 6, 9]

large_seen = None

for number in myList:
    if large_seen is None or large_seen < number:
        large_seen = number
    else:
        continue

print large_seen