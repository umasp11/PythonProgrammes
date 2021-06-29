#String Reverse
s='python'
print(s[::-1])

#Using while loop
s='python'
n=len(s)-1
while n>=0:
    print(s[n], end='')
    n=n-1
print()


# reverse order of words
s=input('enter some string')
l=s.split()
l1=[]
i=len(l)-1
while i>=0:
    l1.append(l[i])
    i=i-1
output=' '.join(l1)
print (output)


#reverse internal content  of each word:
s=input('enter some string')
l=s.split()
l1=[]
i=0
while i<len(l):
    l1.append(l[i][::-1])
    i=i+1
output=' '.join(l1)
print(output)