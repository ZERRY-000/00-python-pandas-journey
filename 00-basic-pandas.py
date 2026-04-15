import pandas as pd
import math

data = {
    'user': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Henry', 'Iris', 'Jack',
             'Kelly', 'Liam', 'Mia', 'Noah', 'Olivia', 'Peter', 'Quinn', 'Rachel', 'Sam', 'Tina'],
    'province': ['Bangkok', 'Bangkok', 'Chiang Mai', 'Bangkok', 'Phuket', 
                 'Chiang Mai', 'Bangkok', 'Phuket', 'Chiang Mai', 'Bangkok',
                 'Phuket', 'Bangkok', 'Chiang Mai', 'Bangkok', 'Phuket',
                 'Chiang Mai', 'Bangkok', 'Phuket', 'Chiang Mai', 'Bangkok'],
    'age': [25, 34, 28, 45, 31, 29, 52, 38, 27, 41,
            33, 26, 48, 35, 30, 44, 39, 28, 50, 32],
    'income': [35000, 48000, 32000, 65000, 42000, 
               38000, 75000, 55000, 30000, 62000,
               45000, 36000, None, 58000, 47000,
               None, 68000, 43000, 52000, 40000],
    'spending': [25000, 35000, 28000, 45000, 38000,
                 32000, 55000, 48000, 25000, 50000,
                 40000, 30000, 42000, 48000, 42000,
                 38000, 52000, 39000, 45000, 35000],
    'debt': [50000, 120000, 0, 200000, 80000,
             30000, 150000, 95000, 0, 180000,
             100000, 45000, 70000, None, 88000,
             110000, 175000, 92000, 140000, 65000]
}

df = pd.DataFrame(data)