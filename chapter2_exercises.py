# Exercises for chapter 2:

# Name: Stephanie Frias

#2.1 In base 8, aka octal, there are only 8 figures to work with: 0, 1, 2, 3, 4, 5, 6, 7. Therefore, 9 is an invalid figure, resulting in a syntax error.
#When we enter 02132, the system believes we are in base eight. Which means (2*1)+(3*8)+(1*64)+(2*512)=1114

#2.2

print 5
x=5
print x+1

#2.3

width = 17
height = 12.0
delimiter = '.'
print width/2
print width/2.0
print height/3
print 1+2*5
print delimiter * 5

#2.4.1

pi=3.1415926535897932
print 4*(5**3)/3*pi

#2.4.2

print ((24.95*.6)*60)+((59*0.75)+3)

#2.4.3

print (8+(15/60.00))+(21+(36/60.00))+(8+(15/60.00))
#the above calculates in minutes the sum of all three paced sections and tells us a total of 38.1 minutes elapsed
print .1*60
#the above tells us that 0.1 minutes equals 6 seconds
#So, to arrive at the answer we add 38 minutes and 6 seconds to the time of 6:52:00am and get to 7:30:06am