#Find All File with .txt Extension Present Inside a Directory

import os

for file in os.listdir("my_dir"):
    if file.endswith(".txt"):
        print(file)


#Check file size

file_stat = os.stat('my_file.txt')
print(file_stat.st_size)


#Get the Full Path of the Current Working Directory
print(os.path.abspath(os.getcwd()))


#Get the File Name From the File Path

file_name = os.path.basename('/root/file.ext')      # file name with extension

print(os.path.splitext(file_name)[0])       # file name without extension


