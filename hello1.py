num=int(input("Enter a number:"))
if(num==1):
    print("Number is not a prime")
    
if num > 1:
    for i in range(2,num):
        if num%i==0:
         print("Number is not a prime")
         break
            
       
else:
    print("Number is Prime")
            
            
