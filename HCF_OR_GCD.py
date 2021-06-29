#highest common factor (H.C.F) or greatest common divisor (G.C.D) of two numbers is the largest positive integer that perfectly divides the two given numbers. For example, the H.C.F of 12 and 14 is 2.

def num(x,y):
    if x>y:
        small=y
    else:
        small=x

    for i in range (1, small+1):
        if (x%i==0 and y%i==0):
            hcf=i
    return hcf

x,y=64,72
print('the HCF is:', num(x,y))