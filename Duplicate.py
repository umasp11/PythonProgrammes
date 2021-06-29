#Remove duplicate from string
d= 'helloo'
r=''
for i in d:
    if i not in r:
        r=r+i
print(r)


#Remove duplicate from list
d= [1,3,1,2,3,5,1,2]
r=[]
for i in d:
    if i not in r:
        r.append(i)
print(r)


# find the duplicate from list
string= [1,3,1,2,3,5,1,2]
dup=[]
for char in string:
    if string.count(char)>1:
        if char not in dup:
            dup.append(char)

print(dup)


# find the duplicate from string
s='Hello world'
dup=''
for c in s:
    if s.count(c)>1:
        if c not in dup:
            dup=dup+c
print(dup)


#Duplicate count
MyList = ("a", "b", "a", "c", "c", "a", "c")
my_dict = {i: MyList.count(i) for i in MyList}
print (my_dict)

#OR

lst = ["a", "b", "a", "c", "c", "a", "c"]
temp=set(lst)
result={}
for i in temp:
    result[i]=lst.count(i)
print (result)

# Remove odd duplicate from a list
li=[12,10,30,33,11,13,15,13,33]
l1=[]

for i in li:
    if i%2==1:
        if i not in l1:
            if li.count(i)>1:
                l1.append(i)
print(l1)
