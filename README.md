# KnowledgeGraph
파이킨 깃헙 : https://github.com/pykeen/pykeen
## 기초 시작
1. sklearn 설치 및 환경 구성 (pykeen 설치를 위해선 sklearn 필요)
```
python -m venv sklearn-env # sklearn-env 라는 환경 만들기
sklearn-env\Scripts\activate  # 가상환경 실행. Mac의 경우 source sklearn-env/bin/activate
pip install -U scikit-learn # 가상환경에 sklearn 패키지 설치
```
2. pykeen 설치(안정 구동을 위해선 파이썬 3.9이상 권장)(해보니까 3.13 이상 버전은 pytorch 같은 다른 패키지 설치가 어려워서 3.12 권장)
```
pip install pykeen
```
2-1. pykeen 설치 시, sklearn 관련 오류.(<- python 3.12로 설치하면 발생 안함)

   pykeen은 구버전 sklearn을 요구하는데 위에 sklearn 설치 방법은 새로운 버전을 설치함. 구버전은 sklearn을 찾지만 신버전은 scikit-learn임.
   
   따라서 환경변수를 사용하여 강제로 검사를 통과시켜야함

### window의 경우
```
set SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL=True
pip install pykeen
```
### mac or linux의 경우
```
export SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL=True
pip install pykeen
```
----

## 간단한 예시
이 예시는 TransE 모델이 Nation 데이터 셋을 사용하여 학습한다. result의 metrics_results를 출력하여 성능 확인
### main
```
from pykeen.pipeline import pipeline

result = pipeline(
    model='TransE',
    dataset='nations',
)

print(result.metric_results.to_df())
```
