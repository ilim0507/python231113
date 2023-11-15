# DemoFormat.py

for i in range(11):
    url = "http://multi.com/?page=" + str(i)
    print(url)

print("---숫자 출력---")
for x in range(1,6):
    print(x,"*",x,"=",x*x)

print("---오른쪽 출력---")
for x in range(1,6):
    print(x,"*",x,"=",str(x*x).rjust(3))

print("---0으로 채우기---")
for x in range(1,6):
    print(x,"*",x,"=",str(x*x).zfill(5))

#파일 쓰기
f = open(r"c:\work\test.txt","wt",encoding="utf-8") #"wt" always overwrites the previous file
f.write("first line\nsecond line\nthird line\n")
f.close()

#파일에 첨부
f = open("c:\\work\\test.txt","a+",encoding="utf-8") #"a+" appends on the existing file
f.write("additional line\n")
f.close()

#파일 읽기
f = open("c:\\work\\test.txt","rt",encoding="utf-8")
print(f.read())
#f.close()

f.seek(0)#다시 처음으로 리셋
result = f.readlines()
for item in result:
    print(item, end="")

f.seek(0)#다시 처음
print(f.readline(), end="")
print(f.readline(), end="")

f.close()

#서식 지정
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:,}".format(15000))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))
