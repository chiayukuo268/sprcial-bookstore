import streamlit as st
import requests

def getAllBookstore():
    url = 'https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M' # 在這裡輸入目標 url
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    res = response.json()
    return res
# 將 response 轉換成 json 格式
# 回傳值

def getCountyOption(items):
    optionList = []
    # 創建一個空的 List 並命名為 optionList
    for item in items:
        # 把 cityname 欄位中的縣市名稱擷取出來 並指定給變數 name
        # hint: 想辦法處理 item['cityName'] 的內容
        name = item['cityName'][0:3]
        if name not in optionList:
            optionList.append(name)
        # 如果 name 不在 optionList 之中，便把它放入 optionList
        # hint: 使用 if-else 來進行判斷 / 用 append 把東西放入 optionList
    return optionList

def getSpecificBookstore(items, county, districts):
    specificBookstoreList = []
    for item in items:
        name = item['cityName']
        # 如果 name 不是我們選取的 county 則跳過
        # hint: 用 if-else 判斷並用 continue 跳過
        if county in name: continue
        specificBookstoreList.append(item)
    return specificBookstoreList

def getBookstoreInfo(items):
    expanderList = []
    for item in items:
        expander = st.expander(item['name'])
        expander.image(item['representImage'])
        expander.metric('hitRate', item['hitRate'])
        expander.subheader('Introduction')
        # 用 expander.write 呈現書店的 Introduction
        expander.subheader('Address')
        # 用 expander.write 呈現書店的 Address
        expander.subheader('Open Time')
        # 用 expander.write 呈現書店的 Open Time
        expander.subheader('Email')
        # 用 expander.write 呈現書店的 Email
        # 將該 expander 放到 expanderList 中
    return expanderList

def app():
    bookstorelist = getAllBookstore()
    countyOption = getCountyOption(bookstorelist)

    st.header('特色書店地圖')
    st.metric('Total bookstore', len(bookstorelist))
    county = st.selectbox('請選擇縣市', countyOption)
    specificBookstore = getSpecificBookstore(bookstorelist, county)
    num = len(specificBookstore)
    st.write(f'總共有{num}項結果', num)


if __name__ == '__main__':
    app()


#python -m streamlit run app.py
#python3 -m streamlit run app.py
#streamlit app.py