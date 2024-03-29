프로젝트 명 : 뉴스 빅데이터를 통한 이슈 키워드 분석
---

- **프로젝트 소개**

  - **목적**
    - 2017년 네이버 검색어 알고리즘 조작 의혹 사실이 드러나며, 2020년 다음, 2021년 네이버의 순서로 실시간 검색어 기능이 폐지되며, 곧이어 뉴스 빅데이터 분석 플랫폼인 빅카인즈가 구축되었지만, 잘못된 전처리로 인한 결과 오류를 확인하였음
    - 따라서 뉴스 웹크롤링을 통해, 다양한 기준에 따른 키워드 분석을 수행하고 시각화함으로써, 사회적 이슈 파악을 용이하게 하고자 함

  - **기대효과**
    - 시장조사 참고자료 활용 가능
    - 비정형 텍스트를 분석 가능한 정형 데이터로 바꾸어 사회 현상을 분석 할 수 있는 기초 자료 제공
    - 방대한 뉴스 정보 속 핵심 키워드 도출 

  - **수집기간**
    - 2022년 09월 01일 ~ 2023년 08월 31일 (1년) 

  - **수집 대상**
    - 다음 주요 뉴스(1Day : 40page), 사건/사고, 경제, 복지, 서울, 수도권(ALL Page)

  - **분석량**
    - Main News : 1.6GB
    - Category News : 1.2GB (사건/사고 + 경제 + 복지 + 서울 + 수도권) 

  - **분석방법**
    - 단어 빈도 분석, 시각화(graph, wordcloud)

  - **수행일정**
    
    　 <img src="https://github.com/JEMinn/Web-crawling-Wordcloud/assets/160000163/e087e7ab-c364-4f81-90f1-37b95bdf4671"  width="600" height="250"/>

  - **업무 흐름 및 설명**
    
    <img src="https://github.com/JEMinn/Web-crawling-Wordcloud/assets/160000163/8293a087-a528-4954-b481-50b614f6dd86"  width="600" height="250"/>

---

- **내용 소개**

  - **데이터 수집 및 전처리**
    - 사건/사고, 경제, 서울, 수도권, 복지 5가지 카테고리 BeautifulSoup 기반 Web Crawling
    - 명사 추출 / 1음절 단어 제외 / 불용어 사전 제작 / 불용어 제외

  - **데이터 분석**
    - Word Count / Word Cloud
      
      <img src="https://github.com/JEMinn/Web-crawling-Wordcloud/assets/160000163/d3cd4e7d-6966-4366-8053-93d8e7ee13f6"  width="200" height="120"/>

  - **분석 결과**
    - 전체 뉴스 Hot Topic
    - 계절별 Hot Issue
    - Category Hot Keyword



