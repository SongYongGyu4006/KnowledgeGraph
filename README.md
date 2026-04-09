# KnowledgeGraph
파이킨 깃헙 : https://github.com/pykeen/pykeen
## 기초 시작
1. sklearn 설치 및 환경 구성 (pykeen 설치를 위해선 sklearn 필요)
```
python -m venv sklearn-env
sklearn-env\Scripts\activate  # activate 
pip install -U scikit-learn
```
2. pykeen 설치(안정 구동을 위해선 파이썬 3.9이상 권장)
```
pip install pykeen
```
----

## 가장 간단한 예시
이 예시는 TransE 모델이 Nation 데이터 셋을 사용한다. 
```
from pykeen.pipeline import pipeline

result = pipeline(
    model='TransE',
    dataset='nations',
)
```
