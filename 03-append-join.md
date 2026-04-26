# Exercises (1-10)

## Concat/Append (Questions 1-4)

1. Combine df_employees and df_new_employees into a single DataFrame (stacked vertically)
2. Combine df_employees and df_new_employees, then reset the index so it starts from 0, 1, 2, 3...
3. Combine only the name and department columns from df_employees and df_new_employees
4. Check how many total rows there are after combining df_employees and df_new_employees


## Merge/Join (Questions 5-10)

5. Join df_employees with df_salary using emp_id (inner join — keep only matching rows from both sides)
6. Join df_employees with df_salary keeping all employees; if no salary exists, set it as NaN (left join)
7. Join df_employees with df_departments to see which floor each person is on
8. Join df_employees with df_salary and df_departments all together (3 tables at once)
9. Join df_employees with df_sales and filter to keep only employees who have sales (inner join)
10. Join df_employees with df_salary (left join), then fill NaN values in the salary column with 0