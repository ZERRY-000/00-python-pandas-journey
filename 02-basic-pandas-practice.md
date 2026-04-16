# 20 โจทย์ฝึก Pandas
## ระดับง่าย (1-10) - Basic Stats & Simple Operations

หาอายุเฉลี่ยของคนทั้งหมด
หารายได้สูงสุดและต่ำสุด
หาค่าใช้จ่ายเฉลี่ยของคนทั้งหมด
นับว่ามีคนกี่คนที่มีหนี้เป็น 0
หาค่าเฉลี่ยของ age, income, spending พร้อมกัน
หาผลรวมของหนี้ทั้งหมด
หาค่ามัธยฐาน (median) ของรายได้
นับว่ามีข้อมูล missing (None) ในคอลัมน์ income กี่แถว
หาส่วนเบี่ยงเบนมาตรฐาน (std) ของอายุ
หาค่าใช้จ่ายรวมทั้งหมดของคนทั้งหมด


## ระดับกลาง (11-20) - GroupBy & Advanced

หาอายุเฉลี่ยของคนในแต่ละจังหวัด
หารายได้เฉลี่ยของคนในแต่ละจังหวัด
นับว่าแต่ละจังหวัดมีคนกี่คน
หาค่าใช้จ่ายรวมของแต่ละจังหวัด
หาจังหวัดที่มีรายได้เฉลี่ยสูงสุด
หาอายุสูงสุดและต่ำสุดในแต่ละจังหวัด (ให้ได้ทั้ง max และ min พร้อมกัน)
หาค่าเฉลี่ยของทั้ง income, spending, debt ในแต่ละจังหวัด (ใช้ agg)
หาว่าแต่ละจังหวัดมีคนที่มีหนี้มากกว่า 100,000 กี่คน
หาจังหวัดที่มีค่าใช้จ่ายเฉลี่ยต่ำสุด
หาความแตกต่างระหว่างรายได้เฉลี่ยและค่าใช้จ่ายเฉลี่ยในแต่ละจังหวัด

# 20 Pandas Practice Problems
## Easy Level (1-10) - Basic Stats & Simple Operations
"These problems focus on basic descriptive statistics and simple column-wise operations."

Find the average age of all individuals.

Find the maximum and minimum income.

Find the average spending of all individuals.

Count how many people have zero debt.

Calculate the mean for age, income, and spending simultaneously.

Calculate the total sum of all debt.

Find the median income.

Count how many missing values (NaN/None) are in the income column.

Find the standard deviation (std) of the age.

Calculate the total spending of everyone combined.

## Intermediate Level (11-20) - GroupBy & Advanced
"These problems focus on data aggregation, grouping, and more complex logic."

Find the average age grouped by each province.

Find the average income for each province.

Count the number of people residing in each province.

Calculate the total spending for each province.

Identify the province with the highest average income.

Find both the maximum and minimum age for each province in a single operation.

Calculate the average of income, spending, and debt for each province using the .agg() method.

Count how many people in each province have a debt greater than 100,000.

Identify the province with the lowest average spending.

Calculate the difference between the average income and the average spending for each province.