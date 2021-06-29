#MAX
arr=[15,5,45,60,30,20]
max=arr[0]

for i in arr:
    if i>max:
        max=i
print(max)

#method2
list=[15,25,45,60,30,20]
list.sort()
print(list[-1])

#Min
arr=[15,5,45,60,30,20]
n= len(arr)
min= arr[0]

for i in range (1, n):
    if arr[i]<min:
        min=arr[i]
print(min)

#method2
list=[15,25,45,60,30,20]
list.sort()
print(list[0])

s='welcome to python'
s1=s.split()
n=len(s1)-1
l=[]

while n>0:
    l.append(s1[n])
    n=n-1
op= ' '.join(l)
print(l)
