# requests을 통해서 원하는 페이지에 접속을 해서 정상적으로 정보를 받아왔는지 확인하고 파일을 만듦
import requests
res = requests.get("http://google.com")
# res = requests.get("http://nadocoding.tistory.com")

print("응답코드 : ",res.status_code) # 200 이면 정상 

# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드 ",res.status_code,"]")

res.raise_for_status() # 문제가 생겼을 때 바로 오류를 내뱉고 프로그램을 끝냄
print("웹 스크래핑을 진행합니다")

# 쌍으로 쓴다
#res = requests.get("http://naver.com")
# res.raise_for_status() # 문제가 생겼을 때 바로 오류를 내뱉고 프로그램을 끝냄

print(len(res.text))
print(res.text)

with open("mygoogle.html","w",encoding="utf8") as f:
    f.write(res.text)