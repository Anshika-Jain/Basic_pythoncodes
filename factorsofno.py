print("Enter the no. to find its factors")
a=int(input())
c=0;

for i in range(2,a):
    if a%i==0:
        c=c+1;
        print(i)
        i=i+1

if c==0:
    print("No factors")
        
