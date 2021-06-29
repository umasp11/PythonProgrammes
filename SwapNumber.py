num1= 10
num2= 20

print('before swaaping num1 value is:', num1)
print('before swaaping num2 value is:', num2)

temp= num1
num1= num2
num2= temp

print('after swaaping num1 value is:', num1)
print('after swaaping num2 value is:', num2)

#Approach2 shortcut
num1,num2= num2,num1
print(num1)
print(num2)


# swap number in a list Approach1
#arr=[15,5,45,60,30,20]
#arr[0],arr[-1]=arr[-1],arr[0]
#print(arr)


# swap number in a list Approach2
arr=[15,5,45,60,30,20]

n=len(arr)

temp=arr[0]
arr[0]=arr[-1]
arr[-1]=temp

print(arr)
print(arr)