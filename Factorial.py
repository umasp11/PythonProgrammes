'''Approach1
num=5

fact=1

for i in range (1, num+1):
    fact=fact*i
print(fact)
'''


#Approach2
def fact(n):
    f=1
    for i in range (1, n+1):
       f=f*i
    print(f)

fact(5)

# function using return method
def fact(n):
    f=1
    for i in range (1, n+1):
       f=f*i
    return f
x=6
result= fact(x)
print(fact(x))