# DemoStr.py

print(dir(str))

strA = "python is enjoyable than my job"
strB = "i hate my job"

print(len(strA))
print(len(strB))
print(strA.capitalize())
print(strA.count(" "))
print(strA.startswith("py"))
print(strA.endswith("on"))

print("---알파벳과 숫자로 구성---")
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("ㅇ너ㅏ멍".isalnum())
print("2580".isdecimal())

data = "<<< I want ramen >>>"
result = data.strip("<> ")
print(data)
print(result)
result = result.replace("ramen", "pizza")
print("Convert")
print(result)
lst = result.split()
print(lst)
print("Combine")
print(":)".join(lst))

#반복문자열 생성
names = ["Ian", "Harry", "Tina"]
for name in names:
    print("Hello {0}, come to GeekStar".format(name))
    print("=" * 40)