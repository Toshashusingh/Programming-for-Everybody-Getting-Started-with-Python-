
hrs=input("Enter Hours:")
try:
    h=float(hrs)
    rate=input("Enter Rate:")
except:
    print("Enter number not string")
    quit()

r=float(rate)
if h<40:
    pay=h*r
else:
    pay=40*r+(h-40)*r*1.5
print(pay)
