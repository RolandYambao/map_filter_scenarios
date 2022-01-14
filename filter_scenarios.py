# Scenario 1
#display blazers scores that are over 100(sterling)
scores = [123, 45, 99, 101, 654, 1, 77, 105, 190]

def scores_over_100(score):
    if score > 100:
        return True
    else:
        return False
over_100_array = list(filter(scores_over_100, scores))
print("these are some high scores", over_100_array)

under_100_array = list(filter(lambda x: x < 100, scores))
print("these guys need more points", under_100_array)

# Scenario 2
comments = ["Hello", "Hello Again", "Goodbye", "Goodbye Again", "No"]
def again_comment(again):
    for i in again.split():
        if i == 'Again':
            return i
again_comments = list(filter(again_comment, comments))
print('AGAIN COMMENTS', again_comments)

# Scenario 3
#verify if a username is taken(masa)
usernames = ['diablo666', 'ghostRiderNicCage', 'weewooACAB']

def does_username_exist(username):
    for i in range(len(usernames)):
        if username == usernames[i]:
            print('Username already exists')
            return True
        else:
            print("Username is yours for the taking")
            return False
print(does_username_exist('diablo666'))
print(does_username_exist('whoGoesThere21'))

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
#splitting a more chaotic list into smaller organized lists (cameron)
stuff = [79.99, 'Shirt', 45.23, 'Pants', True, 'Cat', 666.666, False]

def sort_stuff(arr):
    for i in range(len(arr)):
        thing = arr[i]
        numbers = []
        strings = []
        booleans = []
        if thing == int:
            numbers.append(thing)
        elif thing == str:
            strings.append(thing)
        elif thing == bool:
            booleans.append(thing)
    return numbers, strings, booleans
print("sorted things?", sort_stuff(stuff))

