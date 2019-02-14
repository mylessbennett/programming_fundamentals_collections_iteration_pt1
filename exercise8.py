expenses = [2.00, 10, 159.00, 42, 1.50, 15]

def add_expenses(expenses):
    total = 0
    for cost in expenses:
        total = total + cost
    return total

total_expenses = add_expenses(expenses)
print(total_expenses)
