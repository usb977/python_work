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

print("The table hasn't come yet, so I can only invite 2 guests!")
invited_list.pop(4)
invited_list.pop()
invited_list.pop(0)
invited_list.pop(0)
invited_list.pop(0)
print(invited_list)

for guest in invited_list:
    print(f"{guest}, you are still welcomed on Saturday night!")
del invited_list[0]
del invited_list[0]
print(invited_list)