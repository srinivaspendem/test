print ("Enter the valuse of the quadratic equation: A, B & C", end=' ')
a=float(input())
b=float(input())
c=float(input())
d=float((b**2))
e=float(4*a*c)
f=float(d-e)
if f<=0:
    f=-f
    g=float((f**0.5)/2)
    b=b/2
    print(f"The roots are {b} + i{g}, and {b} - i{g}")
else:
    g=float((f**0.5))
    h=float(-b+g)
    i=float(-b-g)
    j=float(h/(a*2))
    k=float(i/(a*2))
    print (f"The roots are {j} & {k}.")