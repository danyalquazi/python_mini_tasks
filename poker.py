listb = []
listw = []
print("Values are: 2,3,4,5,6,7,8,9,T,J,Q,K,A and Suits are C,D,H,S")
print("First five for black and remaining five for White")
print("Five for white")
n = 5
for i in range(0,n):
	val = input()
	if val not in listb:
		listb.append(val.upper())
	else:
		print("Same cards cannot be repeated enter some other card")
		#n = n+1
print("Five for black")
for i in range(0,n):
	val = input()
	if val not in listw:
		listw.append(val.upper())
	else:
		print("Same cards cannot be repeated enter some other card")
		#n = n+1
print(listb)
print(listw)
