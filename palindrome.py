'''
Given the file, find all the palindromes.
Print the palindromes in order of length.
'''

file = open('/Users/aatishk/PycharmProjects/python_files/palindrome')
sentence = file.read()
sentence = ''.join(sentence.split())

def palindrome(text):

    result = set()

    for index, letter in enumerate(text):

        # To check odd length palindromes
        left, right = index - 1, index + 1
        while left >= 0 and right < len(text) and text[left] == text[right]:
            result.add(text[left:right+1])
            left = left - 1
            right = right + 1

        # To check even length palindromes
        start, end = index, index + 1
        while start >= 0 and end < len(text) and text[start] == text[end]:
            result.add(text[start:end+1])
            start = start - 1
            end = end + 1

    return list(result)

for word in sorted(palindrome(sentence), key=len):
    print word