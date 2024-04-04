import pandas as pd
import numpy as np

# 데이터프레임 생성
df = pd.DataFrame({'income': [np.nan, 3, 4, 5, 8, 9, np.nan]})

# 함수 적용
df['income'].apply(lambda x: np.random.randint(0, 345) if pd.isnull(x) else x)

print("결과값:")
print(df['income'])
