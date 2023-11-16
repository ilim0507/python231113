# DemoForm2.py
# DemoForm2.ui (화면단) + DemoForm2.py (로직단)

import sys
import typing

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QWidget

#웹서버와 통신
import requests
#크롤링
from bs4 import BeautifulSoup

#디자인파일 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]

#폼클래스 정의 (QMainWindow변경)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("Initialize")
    def firstClick(self):
        url = "https://www.daangn.com/fleamarket/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")

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

        self.label.setText("Carrot Crawling")

    def secondClick(self):
        self.label.setText("Second Button")
    def thirdClick(self):
        self.label.setText("Third Button")

#직접 모듈을 실행한 경우면 실해
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()
