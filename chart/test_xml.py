import requests, bs4
import pandas as pd
from lxml import etree
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
import chart
import numpy as np
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chart.settings")

import django
django.setup()

from graph.models import Covid

# 1. URL 파라미터 분리하기.
# Service URL
xmlUrl = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=WRvGBkn9UEtw%2BAsg0tYo210Etxvb1QEcAX%2BwfWvOxVGYJkh1CNZ%2FY4QFa0r7j4bhT4NjPu7z1i1ck8ZgsKMt2Q%3D%3D&pageNo=1&numOfRows=10&startCreateDt=20200101&endCreateDt=20210407'

My_API_Key = "WRvGBkn9UEtw%2BAsg0tYo210Etxvb1QEcAX%2BwfWvOxVGYJkh1CNZ%2FY4QFa0r7j4bhT4NjPu7z1i1ck8ZgsKMt2Q%3D%3D"

response = requests.get(xmlUrl).text.encode('utf-8')
xmlobj = bs4.BeautifulSoup(response, 'lxml-xml')
#print(xmlobj)


rows = xmlobj.findAll('item')
#print(rows)
columns = rows[0].find_all()
#print(columns)

# 모든 행과 열의 값을 모아 매트릭스로 만들어보자.
rowList = []
nameList = []
columnList = []

rowsLen = len(rows)
for i in range(0, rowsLen):
    columns = rows[i].find_all()

    columnsLen = len(columns)
    for j in range(0, columnsLen):
        # 첫 번째 행 데이터 값 수집 시에만 컬럼 값을 저장한다. (어차피 rows[0], rows[1], ... 모두 컬럼헤더는 동일한 값을 가지기 때문에 매번 반복할 필요가 없다.)
        if i == 0:
            nameList.append(columns[j].name)
        # 컬럼값은 모든 행의 값을 저장해야한다.
        eachColumn = columns[j].text
        columnList.append(eachColumn)
    rowList.append(columnList)
    columnList = []  # 다음 row의 값을 넣기 위해 비워준다. (매우 중요!!)

result = pd.DataFrame(rowList, columns=nameList)
# print(result.columns)
# print(rowList)
# for i in rowList:
#     print(i)
# print(len(rowList)
# print(len(rowList[400]))
res = []
for i in rowList:
    if len(i) == 14:
        res.append(i)

for i in res:
    a = list(i[5])[:10]
    i[11] = a
for i in res:
    print(i)
    # Covid.objects.create(
    #     accDefRate          = i[0],
    #     accExamCnt          = i[1],
    #     accExamCompCnt      = i[2],
    #     careCnt             = i[3],
    #     clearCnt            = i[4],
    #     createDt            = i[5],
    #     deathCnt            = i[6],
    #     decideCnt           = i[7],
    #     examCnt             = i[8],
    #     resutlNegCnt        = i[9],
    #     seq                 = i[10],
    #     stateDt             = i[11],
    #     stateTime           = i[12],
    #     updateDt            = i[13],
    # )