# Expense tracker app

#variables

print("Welcome to my Expense tracker App.")

expenseName = input(print("Please enter expense name"))
expenseAmount1 = int(input(print("Please enter expense amount:")))
expenseAmount2 = int(input(print("Please enter expense amount:")))
expenseTotal = expenseAmount1 + expenseAmount2

print(f"Expense Name: {expenseName}")
print(f"Expense total:${expenseTotal}")

