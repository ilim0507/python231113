# web2.py
#웹서버와 통신
import requests
#크롤링
from bs4 import BeautifulSoup

url = "https://www.daangn.com/fleamarket/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# posts = soup.find_all("div",attrs={"class":"card-desc"})
# for post in posts:
#     title = post.find("h2",attrs={"class":"card-title"})
#     title = title.text.replace("\n", "")
#     price = post.find("div",attrs={"class":"card-price"})
#     price = price.text.replace("\n", "")
#     address = post.find("div",attrs={"class":"card-region-name"})
#     address = address.text.replace("\n", "")
#     print("{0}, {1}, {2}".format(title, price, address))

#파일 생성
f = open("dangn.txt", "wt", encoding="utf-8")
posts = soup.find_all("div",attrs={"class":"card-desc"})
for post in posts:
    title = post.find("h2",attrs={"class":"card-title"})
    title = title.text.replace("\n", "")
    price = post.find("div",attrs={"class":"card-price"})
    price = price.text.replace("\n", "")
    address = post.find("div",attrs={"class":"card-region-name"})
    address = address.text.replace("\n", "")
    print("{0}, {1}, {2}".format(title, price, address))
    f.write(f"{title}, {price}, {address}\n")
f.close()