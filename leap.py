year=int(input("enter the year:"))
if year%4==0 and year%100!=0:
    print("%d is a leap year")
elif year % 100==0:
    print("%d is not a leap year")
elif year % 400==0:
     print("%d is a leap year")
else:
     print("%d is a leap year") 
