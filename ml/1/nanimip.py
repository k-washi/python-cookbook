import pandas as pd
from io import StringIO

csv_data = '''A, B, C, D
              1., 2., 3., 4.
              5., 6., , 8.
              10., 11., 12., '''

df = pd.read_csv(StringIO(csv_data))
#print(df)
"""
      A     B     C    D
0   1.0   2.0    3.   4.
1   5.0   6.0         8.
2  10.0  11.0   12.     
"""

print(df.isnull().sum())