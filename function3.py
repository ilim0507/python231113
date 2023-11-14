# function3.py

#함수 정의
def setValue(newValue):
    x = newValue
    print("지역변수:", x)

#함수 호출
retValue = setValue(5)
print(retValue)

def swap(x,y):
    return y,x

#호출
print(swap(3,4))

print("---지역변수와 전역변수---")
x = 5
def func1(a):
    return a+x

print(func1(1))

def func2(a):
    x = 1
    return a+x

print(func2(1))

print(globals())

#기본 값이 있는 함수
def times(a=10,b=20):
    return a*b

print(times())
print(times(5))
print(times(5,6))

#키워드인자(매개변수명 기술)
def connectURL(server, port):
    strURL = "http://" + server + ":" + port
    return strURL

print(connectURL("multi.com","80"))
print(connectURL(port="8080",server="multi.com"))

#가변인자
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result: # Removing this line will add the words one by one.
                result.append(x)
    return result

print(union("HAM","EGG"))
print(union("will this randomly print out this sentence one by one?", "1", "yay!"))
# Wrong. It will add one by one only if they are not repetitive. 

#람다 함수
g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))
print((lambda x:x*x)(3))
print(globals())
