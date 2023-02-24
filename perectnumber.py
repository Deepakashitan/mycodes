sum=0
count=0
A=1
while count<=5:
    sum=0
    for i in range(1,A):
        if A%i==0:
            sum=sum+i
       # else:
       #     break
    if sum==A:
        print ("Perfect ", A)
        count+=1
    A+=1
