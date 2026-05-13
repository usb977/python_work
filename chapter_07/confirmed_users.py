unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"正在验证用户: {current_user.title()}")
    confirmed_users.append(current_user)

print('\n以下用户已经通过验证：')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())