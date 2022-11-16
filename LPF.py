n = eval(input("Enter a number"))
i = 2
j = 3
isprime=1
p_factors = 1

while(i<=n/2):
    if(n%i==0):
        for j in range(3,i):
            if(j==i):
                j=j+1
                continue
            if(i%j==0):
                isprime=0
                break
            j=j+1
        if(isprime==1):
            print(i)
            p_factors=i
            #p_factors.append(i)
    i=i+1
#print(p_factors)    
print(p_factors)                    

        