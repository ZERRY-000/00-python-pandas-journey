# Basic DateTime Commands

## 1. Convert String to DateTime

``` python
# Convert a column to datetime
pd.to_datetime(df['date'])

# Convert various formats
pd.to_datetime('2024-01-15')
pd.to_datetime('15/01/2024', format='%d/%m/%Y')
pd.to_datetime('2024-Jan-15')
```


## 2. Extract Parts of a Date
```python
# Extract year
df['date'].dt.year

# Extract month
df['date'].dt.month

# Extract day
df['date'].dt.day

# Extract month name
df['date'].dt.month_name()

# Extract day of the week (0=Monday, 6=Sunday)
df['date'].dt.dayofweek

# Extract day name
df['date'].dt.day_name()

# Extract quarter (Q1, Q2, Q3, Q4)
df['date'].dt.quarter

# Extract the week number of the year
df['date'].dt.isocalendar().week
```

## 3. Date Calculations
```python
# Find how many days ago from today
(pd.Timestamp.now() - df['date']).dt.days

# Add days
df['date'] + pd.Timedelta(days=7)

# Subtract days
df['date'] - pd.Timedelta(days=30)

# Add months
df['date'] + pd.DateOffset(months=1)

# Add years
df['date'] + pd.DateOffset(years=1)
```

## 4. Filter by Date
```python
# Find data in January
df[df['date'].dt.month == 1]

# Find data in 2024
df[df['date'].dt.year == 2024]

# Find data between two dates
df[(df['date'] >= '2024-03-01') & (df['date'] <= '2024-06-30')]

# Find Mondays
df[df['date'].dt.day_name() == 'Monday']
```

## 5. Format Dates
```python
# Convert to string in a specific format
df['date'].dt.strftime('%d/%m/%Y')
df['date'].dt.strftime('%Y-%m-%d')
df['date'].dt.strftime('%d %B %Y')  # 15 January 2024
```


# 10 DateTime Practice Exercises
```python
# Sample data for practice
df_transactions = pd.DataFrame({
    'transaction_date': ['2024-01-05 14:30:00', '2024-01-15 09:15:00', 
                         '2024-02-20 16:45:00', '2024-03-10 11:20:00',
                         '2024-04-05 13:10:00', '2024-05-25 10:30:00',
                         '2024-06-30 15:00:00', '2024-07-14 08:45:00',
                         '2024-08-22 12:30:00', '2024-09-18 14:15:00'],
    'amount': [1500, 2300, 1800, 2100, 1900, 2500, 3200, 2800, 2400, 2600]
})

df_transactions['transaction_date'] = pd.to_datetime(df_transactions['transaction_date'])
```

# Exercises:
1. Create a new column called 'year' from transaction_date
2. Create a new column called 'month' from transaction_date
3. Create a new column called 'day_name' to see what day each transaction occurred
4. Find the total sales amount for each month from df
5. Find the total sales amount for each quarter from df
6. Filter data for June onwards from df
7. Find how many days ago each transaction occurred, counting from today
8. Create a 'next_month' column showing what date is 1 month after each transaction
9. Count how many transactions occurred on weekdays (Mon-Fri)
10. Convert transaction_date to a string in the format 'dd/mm/yyyy HH:MM'

# Answer Key
```python
# 1. Create the year column
df_transactions['year'] = df_transactions['transaction_date'].dt.year

# 2. Create the month column
df_transactions['month'] = df_transactions['transaction_date'].dt.month

# 3. Create the day_name column
df_transactions['day_name'] = df_transactions['transaction_date'].dt.day_name()

# 4. Total sales per month
df['month'] = df['date'].dt.month
df.groupby('month')['sales'].sum()

# 5. Total sales per quarter
df['quarter'] = df['date'].dt.quarter
df.groupby('quarter')['sales'].sum()

# 6. Filter for June onwards
df[df['date'].dt.month >= 6]

# 7. Find how many days ago each transaction occurred
(pd.Timestamp.now() - df_transactions['transaction_date']).dt.days

# 8. Create the next_month column
df_transactions['next_month'] = df_transactions['transaction_date'] + pd.DateOffset(months=1)

# 9. Count transactions on weekdays (0-4 = Mon-Fri)
(df_transactions['transaction_date'].dt.dayofweek < 5).sum()

# 10. Convert to string
df_transactions['transaction_date'].dt.strftime('%d/%m/%Y %H:%M')
```