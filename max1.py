a=input("Enter number1: ")
b=input("Enter number2: ")
c=input("Enter number3: ")

print('Choose an option :' + '\n 1.Find the maximum number' + '\n 2.Find the minimum number')
choose= input('Enter here : ')
def max():

	if(a>b and a>c):
		print(a+'is the largest number')
	elif(b>c and b>a):
		print(b+'is the largest number')
	elif(c>a and c>b):
		print(c+'is the largest number')
	else:
		print('Please enter different values for each number')

def min():
	if(a<b and a<c):
		print(a+'is the smallest number')
	elif(b<c and b<a):
		print(b+'is the smallest number')
	elif(c<a and c<b):
		print(c+'is the smallest number')
	else:
		print('Please enter different values for each number')

if(choose == '1'):
	max()

elif(choose == '2'):
   min()

else:
	print("Enter atleast one option, numerically")
