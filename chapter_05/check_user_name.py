current_users = ['Alice','Bob','Ciri','Dylan','Elise']
new_users = ['DYLAN','Eric','Frank','Galway','Henle']
current_lower_users = []

for current_user in current_users:
    current_lower_users.append(current_user.lower())

for new_user in new_users:
    if new_user.lower() in current_lower_users:
        print(f'The name "{new_user}" have been used, try another name!')
    else:
        print(f'You can use this name: "{new_user}"!')