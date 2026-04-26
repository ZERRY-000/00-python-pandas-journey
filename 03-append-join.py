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