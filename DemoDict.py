# DemoDict.py

device = {"phone":5, "laptop":20, "monitor":20}

print(len(device))
print(device)
#검색
print(device["phone"])
#입력
device['hdmi'] = 11
#삭제
del device['monitor']
#수정
device["laptop"] = 21

for item in device.items():
    print(item)

for k,v in device.items():
    print(k,v)

#전화번호 저장
phone = {"kim":"1111", "lee":"2222", "park":"3333"}
print("kim" in phone)
print("kang" not in phone)
#참조를 전달
p = phone
p["kang"] ="1234"
print(phone)
print(p)
print(id(phone))
print(id(p))