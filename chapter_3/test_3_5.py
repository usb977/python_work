invited_list = ['Katerina','Lux','Ashe','Riven']

for person in invited_list:
    print(f"{person}! Please come to my house for party on Saturday night!")
print("\n")
print("Riven is busy, she won't join the party!\n")

invited_list[3] = 'Ahri'
for person in invited_list:
    print(f"{person}! Please come to my house for party on Saturday night!")