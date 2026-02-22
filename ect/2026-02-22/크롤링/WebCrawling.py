'''
필수 라이브러리 설치
pip install requests
웹 페이지에 접속하여 데이터를 가져오는 라이브러리입니다.
pip install bs4
가져온 HTML 코드에서 원하는 데이터만 골라내는(파싱) 라이브러리입니다.
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

# 1. 원하는 사이트(네이버) 접속 및 HTML 가져오기
html = urlopen("https://www.naver.com")

# 2. BeautifulSoup 객체 생성 (HTML 파싱 준비)
soup = BeautifulSoup(html, "html.parser")

# 과제 1: 웹 페이지의 타이틀(<title>) 출력하기
print("--- 과제 1: 페이지 제목 ---")
print(soup.head.title)

# 과제 2-1: 모든 <a> 태그(링크) 찾아보기 (find_all 사용)
print("\n--- 과제 2-1: 모든 링크 태그 ---")
links = soup.find_all("a")
# 너무 많으므로 상위 5개만 출력해 봅니다.
for link in links[:5]:
    print(link)

# 과제 2-2: 특정 속성을 가진 태그 찾기 (find 사용)
# '쇼핑 블록 바로가기' 링크 찾기
print("\n--- 과제 2-2: 특정 조건을 만족하는 링크 ---")
shopping_link = soup.find("a", {"href": "#shopping"})
print(shopping_link)