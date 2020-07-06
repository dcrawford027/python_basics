# print all integers from 0 to 150
for i in range(151):
    print(i)

# print all multiples of 5 from 5 to 1000
for x in range(5, 1000, 5):
    print(x)

# print intergers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for y in range(1, 100):
    if y % 10 == 0:
        print("Coding Dojo")
    elif y % 5 == 0:
        print("Coding")
    else:
        print(y)

# add odd integers from 0 to 500,000 and print the final sum
sum = 0
for z in range(500000):
    if z % 2 != 0:
        sum += z
print(sum)

# print positive numbers starting at 2018, counting down by fours
for a in range(2018, 0, -4):
    print(a)

# set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum = 2, highNum = 9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 5
highNum = 45
mult = 9
for b in range(lowNum, highNum + 1):
    if b % mult == 0:
        print(b)