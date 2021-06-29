
string = "Hello this Is an Example With cased letters"
d=[]

for x in string:
    if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
        d.append(x)
print(d)


s='totorial'
v='aeiou'
t=0
d=[]
for i in s:
    if i in v:
        d.append(i)
        t=t+1
print(t)
print(d)