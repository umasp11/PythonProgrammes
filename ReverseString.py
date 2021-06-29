#reverse character in a string
s='Hello python programmer'
r=s[::-1]
print(r)

#Find substring in a string
c='python'
if c in s:
    print('substring found')

#reverse word in a string
words= s.split(' ')
str= words[::-1]
print(str)

output= ' '.join(str)
print(output)