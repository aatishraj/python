import sys
import os
import re
import matplotlib.pyplot as plt
import numpy as npy

def traverse_pattern (match_files, keywords):
	count = 0
	compile_key = re.compile(keywords)
	for word in match_files:
		if compile_key.match(word):
			print "matched: " , word
			count += 1
		else: continue
	return count


if len(sys.argv) < 3:
        print "Syntax Usage : python " + sys.argv[0] + " root_dir " + " keyword "
        sys.exit(0)
elif len(sys.argv) > 3:
        	print "Only 2 arguments are allowed "
        	print "Syntax Usage : python " + sys.argv[0] + " root_dir " + " keyword "
        	sys.exit(0)
else:
		if os.path.isdir(sys.argv[1]):
			root_dir = sys.argv[1]
			keyword = sys.argv[2]
		else:
			print "Path" , sys.argv[1] , "is not a directory that exist"
			sys.exit(0)


result = {}
for myroot, mydirs, myfiles in os.walk(root_dir):
	result[myroot] = traverse_pattern(myfiles, keyword)
print result
 
 
graph = npy.arange(len(result))
plt.bar(graph, result.values(), align='center', width=0.5)
plt.xticks(graph, result.keys())
plt.ylim(0, max(result.values())+2)

plt.title('Number of Files with Keyword')
plt.xlabel('Subdirectory Names')
plt.ylabel('Count Values')
plt.show()
