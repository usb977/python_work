bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)                  #打印完整的列表，包括方括号
print(bicycles[0])               #访问列表中的某个元素，输出无方括号
print(bicycles[0].title())       #通过字符串函数，改变输出格式
print(bicycles[-1])              #下标可以是负数

message = f"My first bicycle was a {bicycles[1].title()}."   #列表中的每个单个元素都可以视为变量，可用f字符串转换为字符串
print(message)