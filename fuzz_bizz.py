'''
Write a program which prints out all numbers between 1 and 100.
When the program would print out a number exactly divisible by 4, print "Fuzz" instead.
When it would print out a number exactly divisible by 6, print "Bizz" instead.
When it would print out a number exactly divisible by both 4 and 6, print "Fuzz_Bizz" instead.
'''

for number in xrange(1, 101):
    if number % 6 == 0 and number % 4 == 0:
        print "Fuzz_Bizz"
    elif number % 4 == 0:
        print "Fuzz"
    elif number % 6 == 0:
        print "Buzz"
    else:
        print number