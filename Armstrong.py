num=int(input('enter a number'))
sum=0
temp=num

while temp>0:
    digit=temp%10
    sum= sum+ digit**3      # 3 digit: 153,407   4 digit:1634
    temp= temp//10

if sum == num:
    print('Armstrong number')
else:
    print('not armstrng')