#!/usr/bin/python 
name = raw_input("Enter Your Name: ") 
print name
print "Enter two integers now: "
number1 = int (raw_input())
number2 = int (raw_input()) 
print number1, 
print number2
x = 1
while(x<=10):
	print x
	x+=1
print "Enter two floating point numbers now: "
float1 = float (raw_input())
float2 = float (raw_input())
if (abs(float1) > abs(float2)):
	print float1

elif(abs(float2) > abs(float1)):
	print float2

else:
	print "Tie"

print "Enter two integers now: "
small = int (raw_input())
big = int (raw_input())

if (small > big):
	a = big 
	big = small 
	small = a
elif (small == big):
	print "These two numbers are equal. Try again."

average = 0

n = small

while (n <= big):
	average+=n 
	n+=1
	
print  (float (average)/((big-small)+1))


c=10

for x in xrange(1,c+1):
	for y in xrange(1,c+1):
		print x*y,
	print'\n'
