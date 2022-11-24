import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate
from sklearn.ensemble import RandomForestClassifier
import joblib

# 데이터 로드, 쉼표 제거
veggie = pd.read_csv('./dataset.csv', thousands= ',')
# 필요없는 column 삭제
veggie = veggie.drop(['수집일'], axis=1)
# 결측치 제거 (36개)
veggie.dropna(inplace=True)

data = veggie[['외부 일사량', '내부온도', '내부습도', '내부CO2', '지습']].to_numpy()
target = veggie['품목명'].to_numpy()
train_input, test_input, train_target, test_target = train_test_split(data, target, test_size=0.2, random_state=42)


rf = RandomForestClassifier(n_jobs=-1, random_state=42, n_estimators = 100, max_depth=21, min_samples_leaf=2)
scores = cross_validate(rf, train_input, train_target, return_train_score=True, n_jobs=-1)
rf.fit(train_input, train_target)

joblib.dump(rf, './rf_model.pkl')