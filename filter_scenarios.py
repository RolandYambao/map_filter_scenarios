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
name_1 = ['Joe']
name_2 = ['Mark']
def check_username(name_1, name_2, taken_names):
    for i in taken_names:
        if i == name_1 and i == name_2:
            return "Both Names Taken"
        elif i == name_1 and i != name_2:
            return name_1 + " is Taken"
        elif i != name_1 and i == name_2:
            return name_2 + " is Taken"
        else:
            return "Both Names are not Taken"

check_names = list(filter(check_username, name_1, name_2, taken_user_names))
print(check_names)

# Scenario 5