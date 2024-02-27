from bs4 import BeautifulSoup as bs
import pandas as pd  
import re  
import requests
import pickle
import time
import os 

# 날짜 생성 
dates = pd.date_range("2023-06-01", "2023-06-30")
# 날짜에서 하이픈(-) 제거
kdates = [re.sub('-', '', str(date)[0:10]) for date in dates]
print(kdates) 

def category_crawling(date):
    print('date =', date)
    
    all_news = [] 
    current_page = 1
    last = True
    
    while last == True:
        
        try:            
            # 10 페이지씩 크롤링
            for page in range(current_page, current_page + 10):
                print("page =", page)
                # 각 페이지에 접근
                url = f'https://news.daum.net/breakingnews/economic/industry?page={page}&regDate={date}'
                res = requests.get(url)
                soup = bs(res.text, 'lxml')
                ul = soup.find("ul", {"class": "list_news2 list_allnews"}).findAll("li")
    
                for li in ul:
                    data = li.find("a", {"class": "link_txt"})
                    press = li.find("span", {"class": "info_news"}).text
        
                    news_url = data.get("href")
                    news_res = requests.get(news_url)
                    news_soup = bs(news_res.text, 'lxml')
                    article = news_soup.find("div", {"class": "article_view"}).find("section").findAll("p")[:-1]
                    contents = " ".join([p.text for p in article])
        
                    all_news.append({
                        'title': data.text,
                        'url': news_url,
                        'press': press,
                        'content': contents
                    })
        except Exception as e:
            print('오류내용 :', e)
    
        # "다음" 버튼이 있는지 확인
        try:
            next_button = soup.select_one('.btn_page.btn_next')
        
            # "다음" 버튼이 없으면 종료
            if not next_button:
                print(f'페이지 {current_page}부터 {current_page + 9}까지 크롤링 완료')
                last = False
                # break
            else:           
                # 다음 10 페이지로 이동
                current_page += 10
                
        except:
            print("페이지가 없음")
            
    return all_news
    
    


# 크롤링 
result_crawling = [category_crawling(date) for date in kdates]

# dataframe으로 저장 
df_news = []
for news_list in result_crawling:
    df_news.extend(news_list)
news = pd.DataFrame(df_news)
final_news = news.drop_duplicates(subset='url')
print(f'중복제거된 기사 개수는 {len(news) - len(final_news)}입니다')

# pickle 저장 (path, file name 바꾸기)
path = r'C:\Users\Joanne\Desktop\데이터\파이썬\semi_project\pkl\1년간복지페이지'
with open(path + '/industry_20230601_20230630.pkl', mode='wb') as f:
    pickle.dump(final_news, f)
    
pd.read_pickle(path + '/welfare_20220901_20220930.pkl')
pd.read_pickle(path + '/industry_20230601_20230630.pkl')

# pickle 로드
with open(path + '/welfare_20220901_20230831.pkl', mode='rb') as f:
    data = pickle.load(f)
    print(data)

pd.read_pickle(path + '/welfare_20220901_20230831.pkl')



# 크롤링한 데이터가 있는 폴더

path = r"C:\Users\Joanne\Desktop\데이터\파이썬\semi_project\pkl\1년간복지페이지"


# 폴더 내의 파일 중 특정 확장자 읽기
file_list = os.listdir(path)

pkl_list = [file for file in file_list if file.endswith('.pkl')]

# 전체 데이터를 담을 빈 데이터프레임 만들기

news_welfare = pd.DataFrame()

# 피클 로드 & 데이터 합치기 

for file in pkl_list:
    pk = pd.read_pickle(path + '/' + file)
    news_welfare = pd.concat([news_welfare, pk], ignore_index = True)
    
# 피클 저장
with open(path + '/welfare_20220901_20230831.pkl', mode='wb') as f:
    pickle.dump(news_welfare, f)
    
# 전체 뉴스 데이터 확인하기 
news_welfare.info()

news_welfare.shape # (97569, 4)

news_welfare.head(3)




df = pd.DataFrame(news_welfare, columns=['title', 'url', 'press', 'content'])

# 결과 출력
print(data)

data.to_csv(r"C:\Users\Joanne\Desktop\데이터\파이썬\semi_project\seasonword_민지.csv", index=False, encoding="utf-8")

