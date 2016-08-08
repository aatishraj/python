'''
Find out which word occurs most times in the file
'''

file = open('/Users/aatishk/PycharmProjects/python_files/words')
word_file = file.read().split()

word_dict = {}

for words in word_file:
    word_dict[words] = word_dict.get(words,0) + 1

word_occur = None
word_count = None

for word,count in word_dict.items():
    if word is None or count is None:
        word_occur = word
        word_count = count
    elif count > word_count:
        word_occur = word
        word_count = count
    else:
        continue

print "The word" , "\"" + word_occur + "\"", "occurs" , word_count , "times."