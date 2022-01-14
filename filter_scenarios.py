# Scenario 1
# display blazers scores that are over 100(sterling)
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
# Specific Word of Comments (Roland)
comments = ["Hello", "Hello Again", "Goodbye", "Goodbye Again", "No"]
def again_comment(again):
    for i in again.split():
        if i == 'Again':
            return i
again_comments = list(filter(again_comment, comments))
print('AGAIN COMMENTS', again_comments)

# Scenario 3
# verify if a username is taken(masa)
usernames = ['diablo666', 'ghostRiderNicCage', 'weewooACAB']

# Scenario 4
taken_user_names = ['Bob', 'Jim', 'Joe', 'Bill', 'Name']
def check_username(taken_names):
    name_1 = 'Joe'
    for i in taken_names.split():
        if i == name_1:
            return i

check_names = list(filter(check_username, taken_user_names))
print('Users with the name "Joe"', check_names)
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
# Verify if Username is Taken (Masa)
taken_user_names = ['Bob', 'Jim', 'Joe', 'Bill', 'Name']
def check_username(taken_names):
    name_1 = 'Joe'
    for i in taken_names.split():
        if i == name_1:
            return i

check_names = list(filter(check_username, taken_user_names))
print('Users with the name "Joe"', check_names)

# Scenario 5
# splitting a more chaotic list into smaller organized lists (cameron)
stuff = [
    {'item': 'amazing shirt', 'owner': 'felix da housecat', 'price': 27.99},
    {'item': 'amazing pants', 'location': 'legs', 'price': 44.99},
    {'item': 'amazing top hat', 'price': 27001.99}
]

def sort_stuff(arr):
    items = []
    prices = []
    for i in range(len(arr)):
        thing = arr[i]
        if thing['price']:
            prices.append(thing['price'])
        if thing['item']:
            items.append(thing['item'])
        
    return items, prices
print("sorted things?", sort_stuff(stuff))

