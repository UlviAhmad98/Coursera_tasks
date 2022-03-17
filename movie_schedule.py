movies={'The Godfather':'23:00',
'No Time To Die':'20:30',
'Harry Potter':'12:00'}
print('Hello! Currently the following movies are showing:')
for key in movies:
    print(key)

user_preference=input('What movie would you like to watch?\n')
schedule=movies.get(user_preference)
if schedule==None:
    print('Unfortunately, we are not showing this movie right now.')
else:
    print(user_preference + ' is showing at ' + schedule)
