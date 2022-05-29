num=int(input("enter the range number: "))
i=0
F_val=1
S_val=1
while(i<num):
    if(i<=1):
        next=i
    else:
        next=F_val+S_val
        F_val=S_val
        S_val=next
    print(next)
    i=i+1
         
