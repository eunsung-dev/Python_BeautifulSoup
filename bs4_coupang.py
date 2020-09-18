import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
res = requests.get(url)
print(res.text)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# items = soup.find_all("li", attrs = {"class":re.compile("^search-product")}) # li 태그 중에서 class 정보가 serach-product로 시작하는 모든 li element를 가져옴
# print(items[0].find("div", attrs = {"class":"name"}).get_text())