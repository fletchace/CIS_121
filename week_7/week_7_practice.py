'''
phonebook = {'matt' : 1438, 'ashley' : 1234}
# adding to dictionary: phonebook[key] = value

phonebook['waters'] = 5678
print(phonebook['matt'])
#error: print(phonebook[0]) will look for the name 0
print(phonebook['waters'])
print(phonebook)
for key in phonebook.keys():
    value = phonebook[key]
    msg = f'Name: {key}  Number: {value}'
    print(msg)
'''
table_people = {}
name = ''
while name != 'done':
    name = input('gimmie yr nme: ')
    if name != 'done':
        age = input('wut ur age: ')
        table_people[name] = age
for names in table_people:
    ages = table_people[names]
    print(f'Name: {names}  Age: {ages}')