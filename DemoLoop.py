# DemoLoop.py

# score = int(input("점수를 입력:"))

# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score < 90:
#     grade = "B"
# elif 70 <= score < 80:
#     grade = "C"
# else:
#     grade = "D"

# print("등급은:", grade)

value = 5
while value > 0:
    print(value)
    value -= 1

lst = ["문자열", 100, 3.14]
print(len(lst))
for item in lst:
    print(item)

d = {"apple":100, "orange":200, "kiwi":300}
for k,v in d.items():
    print (k,v)

#수열
lst2 = list(range(1,11))
print(lst2)

years = list(range(2000,2024))
print(years)

days = list(range(1,32))
print(days)

backwards = list(range(2024,2000,-1))
print(backwards)

print("---수동으로 반복---") # Typical for loop with set #
for i in range(10):
    print(i)

print("---break 구문---") # Stop
for i in lst2:
    if i > 5:
        break
    print("items:{0}".format(i))

print("---continue 구문---") # Skip
for i in lst2:
    if i % 2 == 0:
        continue
    print("items:{0}".format(i))

print("---리스트함축---")
print([i**2 for i in lst2 if i > 5])
tp = ("apple", "orange")
print([len(i) for i in tp])

print("---필터링함수---")
itemL = filter(None, lst2)
for i in itemL:
    print(i)

def getBiggerThan20(i):
    return i > 20

itemL = filter(getBiggerThan20, lst2) # Nothing in lst2 is larger than 20 so nothing pops up
for i in itemL:
    print(i)

itemL = filter(lambda a:a>4, lst2) # Nothing in lst2 is larger than 20 so nothing pops up
for i in itemL:
    print(i)