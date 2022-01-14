# Scenario 1

# Scenario 2
comments = ["Hello", "Hello Again", "Goodbye", "Goodbye Again", "No"]
def again_comment(again):
    for i in again.split():
        if i == 'Again':
            return i
again_comments = list(filter(again_comment, comments))
print('AGAIN COMMENTS', again_comments)

# Scenario 3

# Scenario 4
taken_user_names = ['Bob', 'Jim', 'Joe', 'Bill', 'Name']
def check_username(taken_names):
    name_1 = 'Joe'
    for i in taken_names.split():
        if i == name_1:
            return i

check_names = list(filter(check_username, taken_user_names))
print('Users with the name "Joe"', check_names)

# Scenario 5