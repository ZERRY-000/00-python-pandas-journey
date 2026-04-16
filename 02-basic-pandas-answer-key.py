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
print(df)
# # 1
# print("Age average:", df["age"].mean()) 

# # 2
# print("Income minimum:", df["income"].min()) 

# # 3
# print("Income maximum:", df["income"].max()) 
# print("Spending average:", df["spending"].mean()) 

# # 4
# no_dept_condition = (df["debt"] == 0) # row selected
# print("Have no debt:", no_dept_condition.sum())

# # 5
# list_to_average = ["age", "income", "spending"]
# print("Average of age, income, spending:\n", df[list_to_average].mean().round(2))

# # 6
# print("Sum of debt:", df["debt"].sum())

# # 7
# print("Median of income:", df["income"].median())

# # 8
# print("Number of null in income:",df["income"].isnull().sum())

# # 9
# print("Standard deviation of age:", df["age"].std().round(2))

# # 10
# print("Sum of spending:", df["spending"].sum())

# # 11
# print(df.groupby("province")["age"].mean().round(2))

# # 12
# print(df.groupby("province")["income"].mean().round(2))

# # 13
# print(df.groupby("province")["user"].count())
# print(df.groupby("province").size()) # Another Answer

# # 14
# print(df.groupby("province")["spending"].sum())

# # 15
# print(df.groupby("province")["income"].mean().idxmax())
# # or
# # mapper = {
# #     "income": "mean"
# # }
# # print(df.groupby("province").agg(mapper).idxmax())
# # or 
# # ถ้ามีหลายคอลัมน์ ต้องระบุว่าจะเอา idxmax() ของคอลัมน์ไหน:
# # mapper = {
# #     "income": "mean",
# #     "age": "max",
# #     "spending": "sum"
# # }
# # print(df.groupby("province").agg(mapper)["income"].idxmax())

# # 16
# mapper = {
#         "age" : ["min","max"]
# }
# print(df.groupby("province").agg(mapper))

# # 17
# mapper = {
#         "income" : ["mean"],
#         "spending" : ["mean"],
#         "debt" : ["mean"]
# }
# print(df.groupby("province").agg(mapper).round(2))


# # 18
# debt_condition = df["debt"] > 100000
# mapper = {
#         "debt" : ["count"]
# }
# print(df[debt_condition].groupby("province").agg(mapper))
# # or 
# print(df[debt_condition].groupby('province').size())

# # 19
# mapper = {
#         "spending" : ["mean"]
# }
# print(df.groupby("province").agg(mapper).idxmin().iloc[0])
# # or
# print(df.groupby('province')['spending'].mean().idxmin())

# 20
# income_average = df.groupby("province")["income"].mean()
# spending_average = df.groupby("province")["spending"].mean()

# print("Income average:", income_average)
# print("Spending average:", spending_average)
# print((income_average - spending_average).round(2))