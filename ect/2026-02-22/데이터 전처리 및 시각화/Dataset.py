# pip install pandas numpy nltk
# pip install scikit-learn matplotlib seaborn

# 1단계 : 데이터 불러오기
import pandas as pd

# 데이터 불러오기 (파일 경로는 본인의 환경에 맞게 수정)
df = pd.read_csv("ect/2026-02-22/데이터 전처리 및 시각화/IMDB Dataset.csv")

# 상위 5개 데이터 출력하여 로드 확인
print(df.head())


# 2단계 : 텍스트 정제
import re

def clean_text(text):
    # HTML 태그 제거 [cite: 26]
    text = re.sub(r'<.*?>', '', text) 
    # 특수문자 및 구두점 제거 [cite: 28]
    text = re.sub(r'[^\w\s]', '', text) 
    # 숫자 제거 [cite: 30]
    text = re.sub(r'\d+', '', text) 
    # 소문자 변환 및 양끝 공백 제거 [cite: 33, 36]
    return text.lower().strip()

# 모든 리뷰 데이터에 정제 함수 적용
df['cleaned_review'] = df['review'].apply(clean_text)


# 3단계 : 텍스트 변환
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# 필요한 리소스 다운로드
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def preprocess_text(text):
    # 토큰화 (단어 단위 분리) [cite: 64]
    words = word_tokenize(text)
    # 불용어 제거 및 어간 추출 [cite: 59, 78]
    filtered_words = [stemmer.stem(w) for w in words if w not in stop_words]
    return " ".join(filtered_words)

df['processed_review'] = df['cleaned_review'].apply(preprocess_text)


# 4단계 : TF-IDF 벡터화
from sklearn.feature_extraction.text import TfidfVectorizer

# TF-IDF 객체 생성 및 변환
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['processed_review'])

# 추출된 단어 목록 확인
words = vectorizer.get_feature_names_out()


# 5단계 : 데이터 분석 및 시각화
# 리뷰 길이 계산 (단어 수 기준) 
import matplotlib.pyplot as plt
import seaborn as sns

df['review_length'] = df['review'].apply(lambda x: len(x.split()))

# 감정별 리뷰 길이 통계 요약 출력
print("\n[ 감정별 리뷰 길이 통계 ]")
print(df.groupby('sentiment')['review_length'].describe())

# 감정별 리뷰 길이 분포도 시각화 (히스토그램)
plt.figure(figsize=(10, 5))
# 한글 폰트 설정 (환경에 따라 필요할 수 있음)
plt.rcParams['font.family'] = 'Malgun Gothic' 
sns.histplot(data=df, x='review_length', hue='sentiment', multiple='stack', bins=10)
plt.title('감정별 리뷰 길이 분포도')
plt.xlabel('리뷰 길이 (단어 수)')
plt.ylabel('리뷰 수')
plt.show()