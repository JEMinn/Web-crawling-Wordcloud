import os 
import pandas as pd
from konlpy.tag import Okt # 형태소분석기  
okt = Okt() # object

import pickle # pickle file 읽기 
from wordcloud import WordCloud # 단어 구름 시각화 


# 크롤링한 데이터가 있는 폴더

path = r"C:\ITWILL\3_TextMining\semi_project"


# 폴더 내의 파일 중 특정 확장자 읽기
file_list = os.listdir(path)

pkl_list = [file for file in file_list if file.endswith('.pkl')]

# 전체 데이터를 담을 빈 데이터프레임 만들기

news = pd.DataFrame()

# 피클 로드 & 데이터 합치기 

for file in pkl_list:
    pk = pd.read_pickle(path + '/' + file)
    news = pd.concat([news, pk], ignore_index = True)

# 2. 칼럼 선택
content = news['content'] # DF['칼럼명']

type(content) # pandas.core.series.Series : 1차원

content.shape # 

print(content) # index + value

okt = Okt() # 형태소 분석기  


# 3. 문장 추출 : okt 객체에서 사용할 문자열 정규화
sents = [okt.normalize(contents) for contents in content ]

len(sents) 

# 4. 명사 추출 : Okt 클래스 이용 
nouns = [] 

# 문단 -> 문장
for sent in sents :
    #문장 -> 단어
    for noun in okt.nouns(sent): 
        nouns.append(noun) 
        
len(nouns)

# 5. 단어 전처리 : 단어 선정  
final_nouns = [] # 선정 단어  

for noun in nouns :
    # 2절 ~ 5절 명사 선정
    if len(noun) > 1:
        final_nouns.append(noun)

len(final_nouns) 

# list에서 불용어 제거
with open("./불용어리스트_최종.txt", "r", encoding='utf-8') as f:
    remove_file = f.readlines()
    korean_lib = list(map(lambda x: x.replace("\n", ""), remove_file))[:-1]

stopwords = list(set(korean_lib)) 

len(stopwords) 


final_news=[]
for new in final_nouns :
    if len(new) > 1 and new not in (stopwords) :
        final_news.append(new)
   
# 저장
path = r'C:\Users\Joanne\Desktop\데이터\파이썬\semi_project\pkl'
with open(path + '/industry_top10.pkl', mode='wb') as f:
    pickle.dump(final_news, f)
    
pd.read_csv(path + '/season_sameword.csv')

# 로드
with open(path + '/word불용어제거_2차_최종.pkl', mode='rb') as f:
    data = pickle.load(f)
    print(data)
        
# 6. Top50 word  
from collections import Counter  

word_count = Counter(data)
data_top50_word = word_count.most_common(50) # top50 
print(data_top50_word)

# 7. word cloud 
from PIL import Image
from wordcloud import WordCloud
import numpy as np

mask = np.array(Image.open('복지사진1.png'))

wc = WordCloud(font_path=r'C:\Users\Joanne\Desktop\데이터\파이썬\semi_project\EliceDigitalBaeum_TTF\EliceDigitalBaeum_Bold.ttf',
          width=500, height=400,
          max_words=100,max_font_size=150,
          background_color='white', mask=mask, colormap='gnuplot')

wc = wc.generate_from_frequencies(dict(data_top50_word))



import matplotlib.pyplot as plt 

plt.imshow(wc)
plt.axis('off') # 축 눈금 감추기 
plt.show()
plt.savefig(r"C:\Users\Joanne\Desktop\데이터\파이썬\semi_project\'복지사진1.png'", dpi=300)


# pie chart
import matplotlib.font_manager as fm
import seaborn as sb
#plt.rcParams['font.family'] = 'Malgun Gothic'
font_path = r'C:\Users\Joanne\Desktop\데이터\파이썬\semi_project\EliceDigitalBaeum_TTF\EliceDigitalBaeum_Bold.ttf'
font_props = fm.FontProperties(fname=font_path, size=10)
#plt.rcParams['axes.unicode_minus'] =False
labels, values = zip(*data_top50_word)

plt.figure(figsize = (8, 8))
plt.pie(values,labels=labels, autopct = '%.2f%%', startangle = 140, explode=[0.1,0,0,0,0,0,0,0,0,0], colors=sb.color_palette("gnuplot",len(values)),textprops={'fontsize':10,'fontproperties':font_props}) # 파이차트
#plt.title('1년간 welfare 키워드 top10', fontweight='bold', fontsize=20)
#plt.legend(loc = (1, 0.6), title = 'welfare 키워드')
plt.show()


# 도넛차트
import plotly.express as px
import plotly.graph_objects as go


labels, values = zip(*data_top50_word)
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5)])
fig.update_layout(annotations=[dict(text='<b>welfare Top10</b>', x=0.5, y=0.5, font_size=17, showarrow=False)])

fig.write_image("pie_chart.png") # pip install -U kaleido
img = plt.imread("pie_chart.png")

plt.imshow(X=img)
plt.axis('off')


