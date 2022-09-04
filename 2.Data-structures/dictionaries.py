alien_0 = {'color': 'green', 'points': 5} # {KEY1:VALUE1, KEY2:VALUE2...}

print(alien_0)

#Insert NEW VALUE 
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
#Modify ACTUAL VALUE
alien_0['color'] = 'yellow'
#Remove KEY-VALUE
del alien_0['points']
#Looping Through All Key-Value Pairs
user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
#Looping Through All the Keys in a Dictionary
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for name in favorite_languages.keys():
    print(name.title())

#Nesting list in dictionaries
favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
 }
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
#Dictionaries inside of dictionaries
users = {
 'aeinstein': {
 'first': 'albert',
 'last': 'einstein',
 'location': 'princeton',
 },
 'mcurie': {
 'first': 'marie',
 'last': 'curie',
 'location': 'paris',
 },
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
