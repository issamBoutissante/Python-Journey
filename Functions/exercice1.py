def volBoite(x1=-1,x2=-1,x3=-1):
    if x1==-1:return -1
    if x2==-1:
        return x1**3
    elif x3==-1:
        return x1*x1*x2
    return x1*x2*x3
print(volBoite(5.2))
print(volBoite(5.2,3))
print(volBoite(5.2,3,7.4))