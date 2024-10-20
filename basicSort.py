a=[1,4,2,3,6,7,5,0]
n=len(a)
for i in range(0,n):
    for j in range(0,n):
        if(a[i]<a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)