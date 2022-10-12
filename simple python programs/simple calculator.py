print("choose an option \n 1.addition \n 2.subtraction \n 3.multiplication \n 4.division")
a=int(input("enter the option number"))
b=int(input("enter a number"))
c=int(input("enter another number"))

print("the answer is")

if a==1:
    print(b+c)
elif a==2:
    print(b-c)
elif a==3:
    print(b*c)
elif a==4:
    print(b/c)
    
