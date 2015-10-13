from sys import argv
(script, end_number) = argv
i = 0
numbers = []
inc_value = raw_input("Enter increment value: ")
while i < int(end_number):
    print "At the top i is %d" %i
    numbers.append(i)
    
    i = i + int(inc_value)
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
    
    
print "The numbers: "

for num in numbers:
    print num
