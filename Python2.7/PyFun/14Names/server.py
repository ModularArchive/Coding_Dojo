users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

#for name in students:           #If you remove the # in the beginning of line 14 and 15 you will get functioning code for part 1 of assignment
    #print name['first_name'], name['last_name']

print users['instructors']

for item in users:
    print item
    counter = 1
    for person in user{item}:
        print counter, person['first_name'], person['last_name']


for key in users:
    print key
    position = 0
    for person in users[key]:
        position += 1
        name_length = len(person['first_name']) + len(person['last_name'])
        print position, ' - ', person['first_name'].upper(), '', person['last_name'].upper(), '-', names_length

