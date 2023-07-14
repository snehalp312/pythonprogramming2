try:
    x=int(input("Enter a number uto 100"))
    if x>100:
        raise ValueError(x)
except ValueError:
    print(x,"is out oof allowed range")
else:
 p=89
 sum=p+x
 print(sum)