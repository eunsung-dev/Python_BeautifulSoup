import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

# html 문서를 lxml 파써를 통해서 beautifulsoup 객체로 만든 것
soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup은 우리가 가져온 html 모든 문서를 가지고 있는데 그 중에서 첫번째로 발견되는 a 태그를 출력
# print(soup.a.attrs) # a element의 속성 정보를 출력
# print(soup.a["href"]) # a element의 herf 속성 '값' 정보를 출력

# 첫번째로 발견되는 a tag에 대해서
# class = "Nbtn_upload"인 a element 를 찾아줘
# print(soup.find("a",attrs = {"class":"Nbtn_upload"}))
# class = "Nbtn_upload"인 어떤 element를 찾아줘
# print(soup.find(attrs = {"class":"Nbtn_upload"}))

# print(soup.find("li", attrs = {"class":"rank01"}))
rank1 = soup.find("li", attrs = {"class":"rank01"})
# print(rank1.a)
# print(rank1.a["title"])

# 형제로 넘어가는, 다음 태그로 넘어가는
# print(rank1.a.get_text())
# #print(rank1.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank2.a.get_text())
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())

# print(rank1.parent)
# rank2 = rank1.find_next_sibling("li") # next sibling으로 가는데 그 조건에 맞는, next sibling을 몇번해야하는지 신경쓸 필요 없음
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# 형제들 가져오기
# print(rank1.find_next_siblings("li"))

webtoon = soup.find("a",text = "소녀의 세계-2부 19화")
print(webtoon)