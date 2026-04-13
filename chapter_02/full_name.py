#使用f字符串
first_name = 'ada'
last_name = 'lovelace'
full_name = f'{first_name} {last_name}'
print(f"Hello, {full_name.title()}!")

#删除字符串的空白
favorite_language = ' python '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

#删除网址的前缀
nostar_url = 'https://nostarurl.com'
simple_url = nostar_url.removeprefix('https://')
simple_url = simple_url.removesuffix('.com')
print(simple_url)