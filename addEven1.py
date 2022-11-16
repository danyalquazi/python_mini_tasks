print("Range 500-1000")
print("Sum of all the even numbers in the range")
sum1=0
sum2=0
a= 500
for a in range(500,1000):
	if(a%2==0):
		sum1=sum1+a
		a=a+1

	else:
		sum2=sum2+a
		a=a+1

	a=a+1
print("The sum of even numbers is %d"%(sum1))
print("The sum of odd numbers is %d"%(sum2))
