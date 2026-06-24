from pathlib import Path
import json

def get_stored_username(path):
    """如果存储了用户名，就获取它"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
def get_new_username(path):
    """提示用户输入用户名"""
    username = input("请输入您的姓名：")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """问候用户，并指出其姓名"""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"欢迎再次登录，{username}")
    else:
        username = get_new_username(path)
        print(f"您下次登录时，系统仍然会记住您的名字是：{username}")

greet_user()