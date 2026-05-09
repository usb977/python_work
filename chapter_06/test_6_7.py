person_1 ={
    'First':'Ritr',
    'Last':'Fdnks',
    'Age':22,
    'City':'Beijing',
}
person_2 ={
    'First':'Yndcr',
    'Last':'Disnds',
    'Age':28,
    'City':'Paris',
}
person_3 ={
    'First':'Cdms',
    'Last':'Pzfks',
    'Age':19,
    'City':'Hefei',
}

people = [person_1, person_2, person_3]

i=1

for person in people:
    print(f'\n The info of person_{i} is :')
    print(f'\t First : {person['First']}')
    print(f'\t Last : {person['Last']}')
    print(f'\t Age : {person['Age']}')
    print(f'\t City : {person['City']}')
    i=i+1