year=int(input("enter the year to check"))
if year>=1900 and year<=10**5:
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print(True)
            else:
                print(False)
        else:
            print(True)  
    else:
        print(False) 
