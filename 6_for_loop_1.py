expenses = [1200,1300,1444,1900, 3242, 123,443]

for i, expense in enumerate(expenses):
    if expense>1500:
        print(f"Month {i+1} has expense > 1500")
        break

