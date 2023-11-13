# DemoListTuple.py

strA = "when should I quit my job"
print(strA[0])
print(strA[1])
print(strA[0:6])
print(strA[:6])

colors = ['r','g','b']
print(len(colors))
print(type(colors))
colors.append('w')
colors.insert(0,'black')
colors += 'yellow'
print(colors)
colors.pop()
print(colors)
colors.sort()
print(colors)


for item in colors:
    print(item)

print("---Set형식---")
a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

print("---Tuple형식---")
tp = (10,20,30)
print(len(tp))
print(type(tp))

#함수정의
def calc(a,b):
    return a+b, a*b

#호출
result = calc(3,4)
print(result)

print("id:%s, name:%s" % ("limi", "Ian"))

args = (5,6)
print(calc(*args))

print("---형식변환---")
a = set((1,2,3))
print(a)
b = list(a)
print(b)
b.append(4)
print(b)