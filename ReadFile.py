#Read a File Line by Line Into a List
#Using readlines()
with open("data_file.txt") as f:
    content_list = f.readlines()

print(content_list)     # print the list

content_list = [x.strip() for x in content_list]    # remove new line characters
print(content_list)

#Using for loop and list comprehension
with open('data_file.txt') as f:
    content_list = [line for line in f]

print(content_list)

with open('data_file.txt') as f:    # removing the characters
    content_list = [line.rstrip() for line in f]

print(content_list)