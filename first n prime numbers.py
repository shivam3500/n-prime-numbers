x=int(input('How many prime number do you want to print: '))
y=0
z=1
while y<x:
    z+=1
    count=1
    for i in range(2,z):
        if z%i==0:
            count=0
            break
        
    if count==1:
        print(z,end=' ')
        y+=1
