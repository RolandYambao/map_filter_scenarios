# Scenario 1
numbers = [1, 2, 3, 4, 5]
def mathematical_operation(num):
    return num * num - num

result_numbers = map(mathematical_operation, numbers)
print('MATH', list(result_numbers))
    
# Scenario 2

# Scenario 3
drinks = ['Cola', 'Sprite', 'Coffee', 'Tea', 'Water']
result_drink = map(lambda x: x, drinks)
print('DRINK', list(result_drink))

# Scenario 4

# Scenario 5
book_titles = ['A Book', 'Another Book', 'Interesting Book', 'Do Not Read This']
result_book = map(lambda x: x, book_titles)
print('BOOK', list(result_book))