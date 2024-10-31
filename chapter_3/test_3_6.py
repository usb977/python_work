invited_list = ['Katerina','Lux','Ashe','Riven']
print(invited_list)
print("Riven is busy, she won't join the party! Ahri can come!")
invited_list[3] = 'Ahri'
print(invited_list)
print("I have found a big table, so I can invite 3 more guests!\n")

invited_list.insert(0,'Caitlyn')
invited_list.insert(2,'Soraka')
invited_list.append('Seraphine')
print(invited_list)
for person in invited_list:
    print(f"{person}! Please come to my house for party on Saturday night!")