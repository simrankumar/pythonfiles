import random as ran
a=ran.randint(1,9)      
print(a)

for n in range(5):
    b=int(input("enter no"))
    if a<b:
        print("try again",a)
    elif a==b:
        print("successful",a)
    else:
        print("try again",a)
    
 
