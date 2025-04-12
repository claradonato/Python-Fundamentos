import pandas as pd
import numpy as np

# DataFrame de Array
data = ['Alex', 10], ['Bob', 20], ['Saulo', 30]
df = pd.DataFrame(data,columns=['Name', 'Age'])
print(df)

#Serie com padrão RangeIndex
s = pd.Series([1, 3, 2, 3, 5, 3])
print(s)

#DataFrame com Array Numpy com um índice de data-time usando data.range()
dates = pd.date_range("20250101", periods=5)
print(dates)

#Dicionário de objetos onde a chave é a coluna
df2 = pd.DataFrame(
    {
        'A': 1.0,
        'B': pd.date_range('20250101', periods=10),
        'C': pd.Series(1, index=list(range(10)), dtype='float32'),
        'D': np.array([3] * 10, dtype='int32'),
        'E': pd.Categorical(['test', 'train', 'test', 'train', 'test', 'train', 'test', 'train', 'test', 'train']),
        'F': 'foo',
    }
)

print(df2)
df2 = df2.set_index('B') #define a coluna B como índice antes de fatiar
print(df2["20250101":"20250103"])
