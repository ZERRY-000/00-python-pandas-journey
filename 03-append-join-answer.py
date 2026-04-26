import pandas as pd

# DataFrame 1: Employee data
df_employees = pd.DataFrame({
    'emp_id': [101, 102, 103, 104, 105],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'department': ['Sales', 'IT', 'HR', 'Sales', 'IT']
})

# DataFrame 2: Salary data
df_salary = pd.DataFrame({
    'emp_id': [101, 102, 103, 106, 107],
    'salary': [35000, 45000, 38000, 42000, 50000],
    'bonus': [5000, 7000, 6000, 6500, 8000]
})

# DataFrame 3: New employees
df_new_employees = pd.DataFrame({
    'emp_id': [106, 107],
    'name': ['Frank', 'Grace'],
    'department': ['Marketing', 'Finance']
})

# DataFrame 4: Department data
df_departments = pd.DataFrame({
    'department': ['Sales', 'IT', 'HR', 'Marketing'],
    'location': ['Floor 1', 'Floor 3', 'Floor 2', 'Floor 1'],
    'manager': ['John', 'Sarah', 'Mike', 'Lisa']
})

# DataFrame 5: Employee sales data
df_sales = pd.DataFrame({
    'emp_id': [101, 104, 108],
    'sales_amount': [120000, 150000, 90000],
    'quarter': ['Q1', 'Q1', 'Q1']
})



# Concat/Append (Questions 1-4)
# 1. Combine df_employees and df_new_employees
pd.concat([df_employees, df_new_employees])

# 2. Combine and reset index
pd.concat([df_employees, df_new_employees], ignore_index=True)

# 3. Combine only the name and department columns
pd.concat([df_employees[['name', 'department']], 
           df_new_employees[['name', 'department']]])

# 4. Count total rows after combining
len(pd.concat([df_employees, df_new_employees]))
# or
pd.concat([df_employees, df_new_employees]).shape[0]

# Merge/Join (Questions 5-10)
# 5. Inner join (keep only matching rows)
df_employees.merge(df_salary, on='emp_id')

# 6. Left join (keep all employees)
df_employees.merge(df_salary, on='emp_id', how='left')

# 7. Join with the department table
df_employees.merge(df_departments, on='department')

# 8. Join 3 tables at once
df_employees.merge(df_salary, on='emp_id', how='left').merge(df_departments, on='department', how='left')

# 9. Inner join with sales data (keep only employees with sales)
df_employees.merge(df_sales, on='emp_id')

# 10. Left join then fill NaN with 0
df_employees.merge(df_salary, on='emp_id', how='left').fillna(0)