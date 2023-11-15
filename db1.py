# db1.py
import sqlite3

#메모리에서 작업
#연결객체 리턴받기
con = sqlite3.connect(":memory:")
#커서객체 리턴
cur = con.cursor()

#테이블구조 (자료구조 생성)
cur.execute("create table PhoneBook (name text, phoneNum text);")

#1건 입력
cur.execute("insert into PhoneBook values ('Ian', '010-3008-4166');")

#입력 파라미터 처리
name = "harry"
phoneNumber = "010-7771-9990"
cur.execute("insert into PhoneBook values (?,?)", (name, phoneNumber))

#N건 입력
datalist = (("Tina","This dude is being kicked out"), ("Taino", "010-1234-4321"), ("Beomji","lol"))
cur.executemany("insert into PhoneBook values (?,?)", datalist)

#검색
cur.execute("select * from PhoneBook;")

print("---fetchone()---")
print(cur.fetchone())
print("---fetchmany(2)---")
print(cur.fetchmany(2))
print("---fetchall()---")
print(cur.fetchall())

# for row in cur:
#     print(row)