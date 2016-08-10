file = open("/Users/aatishk/PycharmProjects/python_files/mbox-full")

word_dict = {}

for words in file:
    for word in words.split():
        word_dict[word] = word_dict.get(word,0) + 1

word_list = []
for char,count in word_dict.items():
    word_list.append( (count, char) )

word_list.sort(reverse=True)

for count, char in word_list[:5]:
    print "count:" , count , "and word is: \"" + char + "\""