p=int(input("enter the principal"))
r=int(input("enter the rate"))
t=int(input("enter the time"))
Amt=p*(1+(r)/100)**t
ci=Amt-p
print("Simple Interest is: ",ci)