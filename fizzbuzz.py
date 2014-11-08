import sys
upperLimit = 100
if len(sys.argv) > 1:
    upperLimit = int(sys.argv[1])
else:
    upperLimit = int(raw_input("Enter upper limit: "))
    
print "Fizz buzz counting up to {}".format(upperLimit)
for i in range(1,upperLimit+1):
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