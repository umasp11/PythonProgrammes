import random
import calendar

#Print number in randomly
print(random.randint(0,19))

#Leap year
s= 20
if s%4==0:
    print('leap year')
else:
    print('no leap')

#Largest among 3
a,b,c=10,20,30

if a>b and a>c:
    print('a is big')
elif b>c and b>a:
    print('b is big')
else:
    print('c is big')

#Multiplication table
number= 15
for i in range (1,11):
    print(i, 'X', number, ' = ', number*i )

# sum of natural number

total=0
for i in range(1,10):
    total= total+i
print(total)


#Find Numbers Divisible by Another Number
list = [12, 65, 54, 39, 102, 339, 221]
d=[]
for i in list:
    if i%13==0:
        d.append(i)
print(d)

#Convert Decimal to Binary, Octal and Hexadecimal
dec=234

print(bin(dec), 'in binary')
print(oct(dec), 'in octal')
print(hex(dec), 'in hexa')

#Find ASCII Value of Character
n1="A"
n2= 'a'
print(ord(n1))
print(ord(n2))



