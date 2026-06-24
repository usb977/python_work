from pathlib import Path
import json

def get_stored_username(path):
    """如果存储了用户信息，就获取它"""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None
    
def get_new_username(path):
    """提示新用户输入用户信息"""
    user_info = {}
    user_info['name'] = input("请输入您的姓名：")
    user_info['age'] = input("请输入您的年龄：")
    user_info['locale'] = input("请输入您所在的城市名：")

    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info['name']

def greet_user():
    """问候用户，并打印用户信息"""
    path = Path('user_info.json')
    user_info = get_stored_username(path)
    
    if user_info:
        user_assert = input(f"请确认用户名是否为{user_info['name']} yes/no：")
        if user_assert == 'yes':
            print("\n用户的个人信息为：")
            for k,v in user_info.items():
                print(f"\t {k} ：{v}")
        else:
            print("用户核对失败，请重新输入您的信息!")
            user_name = get_new_username(path)
            print(f"您好！系统已经保存好{user_name}的个人信息，下次登录将会显示！")
    else:
        user_name = get_new_username(path)
        print(f"您好！系统已经保存好{user_name}的个人信息，下次登录将会显示！")

greet_user()
