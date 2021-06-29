list= [23,43,45,10]
add=0
for i in list:
    add=add+i

print(add)

print(sum(list))    # method2



#Remove perticular keyword on nth occurance

word= ['uma', 'apex', 'uma', 'aska', 'uma']
rem='uma'
n=3
count=0

for i in range (0, len(word)):
    if word[i]==rem:
        count=count+1
        if count==n:
            del word[i]
print(word)
