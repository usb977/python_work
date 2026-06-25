from name_function import get_formatted_name

print("任何时候输入'q'即可退出程序！")
while True:
    first = input("\n请输入您的名字：")
    if first == 'q':
        break
    last = input("请输入您的姓：")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")