import requests
from bs4 import BeautifulSoup

URL = "https://testing-www.codefellows.org/courses/code-400/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(class_="course-details")
# print(results.prettify())

titles = results.find_all("h3")

for title in titles:
    print(title.text)

anchors = results("a")
