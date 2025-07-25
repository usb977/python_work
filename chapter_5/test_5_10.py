current_users = ['Dylan','Ciri','admin','Frank','Alice']
current_users_for_check = []

for user in current_users:
    current_users_for_check.append(user.lower())
#print(current_users_for_check)

new_users = ['Dylan','Simi','Ciri','Ryu','Faker']

for user in new_users:
    if user.lower() in current_users_for_check:
        print(f'Please input another name, "{user}" have been ingistered!')
    else:
        print(f'Congratulations! "{user}" has not been used!')