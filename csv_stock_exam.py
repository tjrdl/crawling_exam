import requests
import csv
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.naver?sosok=0&page="

filename = "코스피_시가총액1~50_123.csv"
# f = open(filename,"w",encoding="utf-8")
# f = open(filename,"w",encoding="utf-8-sig")
f = open(filename,"w",encoding="utf-8-sig",newline="")
# newline="" : 윈도우에서 csv 파일을 열 때 줄바꿈이 안 되는 문제 해결
writer = csv.writer(f)

# title=  "N 종목명 현재가 전일비 동락률 액면가 시가총액 상장주식수 외국인비율 거래량 PER POR 토론실"
title=  "N 종목명 현재가 전일비 동락률 액면가 시가총액 상장주식수 외국인비율 거래량 PER POR ".split("\t")
writer.writerow(title)

for page in range(1,2):
    res = requests.get(url + str(page))
    res.raise_for_status()  # 에러가 있다면 멈추고 에러를 알려줌
    # 200이면 정상
    soup = BeautifulSoup(res.text, "html.parser")  # BeautifulSoup 객체 생성 # HTML 파싱

    data_rows = soup.find("table",attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        # print("len:",len(columns))
        if len(columns) == 1:
            continue
        data = [column.get_text().strip()for column in columns] # strip():\n,\t 제거
        # print(data)

        writer.writerow(data)
        