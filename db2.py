# db2.py
import sqlite3

#연결객체 리턴받기 (영구적인 파일로 저장)
con = sqlite3.connect("c:\\work\\sample.db")
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
print(cur.fetchall())

#Commit (상기 파일 내 SQL 구문들을 실질적으로 반영) 
con.commit()