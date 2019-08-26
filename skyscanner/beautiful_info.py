# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
doc = input("input file Name:")
#soup = BeautifulSoup(open("skyscanner_RGN.html",encoding="utf-8"), "html.parser")
soup = BeautifulSoup(open(doc,encoding="utf-8"), "html.parser")
print(soup.prettify())