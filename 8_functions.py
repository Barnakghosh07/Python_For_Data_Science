def find_total (expenses):
    total = 0
    for expense in expenses:
        total += expense
    return total

    


expenses_sergey = [30,45,65,90]
expenses_sundar = [10,25,75,80]

total = find_total(expenses_sergey)
print("Sergey's total expense: ", total)

total = find_total(expenses_sundar)
print("Sundar's total expense: ", total)
    
