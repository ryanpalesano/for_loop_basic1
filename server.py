#1.print all integers from 0 to 150
for i in range(0, 151):
  print(i)
#2.print all the multiples of 5 from 5 to 1,000
for i in range(5,1001,5):
    print(i)
#3.print integers to 1 to 100, If possible divide by 5, print "coding" instead. If divisible by 10, print "coding dojo"
for i in range(0, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding Dojo")
    else:
        print(i)
#4. Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for i in range(0, 500001,2):
    sum += i
print(sum)
#5.print postive numbers starting at 2018, counting down by fours
for i in range(2018,0, -4):
    print(i)
"""#6.set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For ex: if lowNum=2, highNum=9,
and mult=3, the loop should print 3,6,9 (on successive lines)"""
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum,highNum + 1):
    if i % mult == 0:
        print(i)
