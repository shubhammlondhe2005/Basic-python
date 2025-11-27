#write a python program to print the content of a directory using the OS module.
import os

directory_path = '/file path'

contents=os.listdir(directory_path)

for item in contents:
    print(item)