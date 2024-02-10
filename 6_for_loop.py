expenses = [1200,1300,1444,1900, 3242, 123,443]

# total_expense = expenses[0] + expenses[1] + expenses[2] +expenses[3]
# print(total_expense)

total_expense = 0
# for expense in expenses:
#     total_expense = total_expense+expense
# print(total_expense)

# for i in range(3, 5):
#     print(i)

for i, expense in enumerate(expenses):
    print(f"Month {i+1}, Expense: {expense} ")
    total_expense += expense
    print("Total Expense is: ", total_expense)
    # print(i+1)
    # print(expenses[i])


