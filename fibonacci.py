'''
given a number by the user find the
fibonacci series till that range.
(recursive call)
'''

def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number-1)+fibonacci(number-2)

try:
    user_input = int(raw_input('Enter a number:'))
    for series in xrange(user_input):
        print fibonacci(series)
except :
    print "Invalid Input. Try again."



