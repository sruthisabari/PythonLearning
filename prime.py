def isprime(n):
    count=0
    for i in range(2,n+1):
        if n%i==0:
            count+=1
    if count==1:
        return True
    else:
        return False

def getprime(n):
    for i in range(1,n+1):
        flag=0
        for j in range(1,i+1):
            if i%j==0:
                flag+=1
        if flag==2:
            print(j)


print(getprime(100))

