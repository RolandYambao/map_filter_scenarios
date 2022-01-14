# Scenario 1
numbers = [1, 2, 3, 4, 5]
def mathematical_operation(num):
    return num * num - num

result_numbers = map(mathematical_operation, numbers)
print('MATH', list(result_numbers))
    
# Scenario 2
#inflation on products increased to 7% (michael)
prices = [9.99, 12.99, 17.99, 33.99]
def increase_7_percent(price):
    return price * 1.07
    
result = list(map(increase_7_percent, prices))
print("price increased 7 percent", result)

result2 = list(map(lambda x: x * 1.07, prices))
print("price increased 7 percent lambda", result2)


# Scenario 3
drinks = ['Cola', 'Sprite', 'Coffee', 'Tea', 'Water']
result_drink = map(lambda x: x, drinks)
print('DRINK', list(result_drink))

# Scenario 4
#total value in a cart (neo)
cart = [17.99, 121.99, 17.99, 38.99]
def cart_total(prices):
    total = 0
    for i in range(len(prices)):
        total += prices[i]
    return total
print("cart total", cart_total(cart))

# Scenario 5
book_titles = ['A Book', 'Another Book', 'Interesting Book', 'Do Not Read This']
result_book = map(lambda x: x, book_titles)
print('BOOK', list(result_book))