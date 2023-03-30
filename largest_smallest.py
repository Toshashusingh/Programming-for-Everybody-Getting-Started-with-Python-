largest=None
smallest=None
ls=[]
while True:
    num=input("Enter a Number:")
    if num== 'done':
        break
    try:
        n=float(num)
    except:
        print("Invalid input")
    
    ls.append(n)
for i in ls:
    if largest is None:
        largest=i
    elif i>largest:
        largest=i
    if smallest is None:
        smallest=i
    
    elif i<smallest:
        smallest=i
print("Maximum is",largest)
print("Minimum is",smallest)