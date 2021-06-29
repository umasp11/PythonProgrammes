#Full Pyrammid
num= int(input('enter a number'))
for i in range(0,num):
    for j in range(0,num-i-1):  # this for loop is to print space before the star
        print(end=' ')
    for j in range (0,i+1):     # this for loop is to print number of star
        print('*', end=' ')     # end=' ' here need to give space
    print()

#Full Pyrammid in reverse
num= int(input('entar a number'))
for i in range (num):
    for j in range(i):
        print(" ", end='')
    for j in range (num-i):
        print('*', end=' ')
    print()

# Right tringle Pyramid
n=int(input('enter number of rows'))
for i in range (1, n+1): # i represents no of rows
      for j in range (i): # j represents no star
          print ('*', end=' ')
      print()

#OR

n=int(input('enter number of rows'))
for i in range (1, n+1):
    print ('*'*i)
