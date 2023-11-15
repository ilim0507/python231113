# DemoOS.py
from os.path import *
import glob
import os

# print(dir())

print(abspath("demo.py"))
print(basename("c:\\work\\demo.py"))

fName = "c:\\python310\\python.exe"
if exists(fName):
    print("file size : {0}".format(getsize(fName)))
else:
    print("file does not exist")

result = glob.glob("c:\\work\\*.py")
for item in result:
    print(item)

print("운영체제이름:{0}".format(os.name))
print("환경변수:{0}".format(os.environ))

# os.system("notepad.exe")

os.chdir("..")
os.chdir("c:\\python310")
result = glob.glob("*.*")
print(result)