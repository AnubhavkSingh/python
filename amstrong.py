n=int(input("enter the number"))
num=n
len=len(str(num))
sum=0
while n!=0:
    r=n%10
    sum=sum+(r**len)
    n=n//10
if num==sum:
    print(num,"is a amstrong number")
else:
    print(num,"is not a amstrong number")        
