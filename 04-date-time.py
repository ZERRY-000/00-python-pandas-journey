import pandas as pd
import numpy as np
 
# Create sample data
df = pd.DataFrame({
    'date': ['2024-01-15', '2024-02-20', '2024-03-10', '2024-04-05', '2024-05-25',
             '2024-06-30', '2024-07-14', '2024-08-22', '2024-09-18', '2024-10-09'],
    'sales': [12000, 15000, 18000, 14000, 16000, 22000, 19000, 21000, 17000, 20000],
    'orders': [45, 52, 61, 48, 55, 78, 65, 72, 59, 68]
})
 
# Convert string to datetime
df['date'] = pd.to_datetime(df['date'])
 