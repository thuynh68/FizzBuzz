print "Fizz buzz counting up to 100"
upperLimit = 101
for i in range(1,upperLimit):
    divisibleByThree = i % 3 == 0
    divisibleByFive = i % 5 == 0     
    if (not divisibleByThree) and (not divisibleByFive):
        print ("%d" % (i))
    elif divisibleByThree and divisibleByFive:
        print "Fizz buzz"
    elif divisibleByThree == True:
        print "Fizz "
    elif divisibleByFive:
        print "buzz"