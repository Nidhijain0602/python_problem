import os
from os.path import isfile, join
arr=os.listdir("F:\check")

def print_all_filepaths(dirpath):
    for f in os.listdir(dirpath):
        if isfile(join(dirpath, f)):
            print(dirpath+"\\"+f)
        else:
            print_all_filepaths(dirpath+"\\"+f)
# print_all_filepaths("F:\check")

add_path=input("enter path")
print()
print_all_filepaths(add_path)

