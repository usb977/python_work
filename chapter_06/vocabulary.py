vocabulary = {
    'constant':'值不会改变的量',
    'variable':'值会改变的量',
    'list':'列表，用来存储数据，可变',
    'tuple':'内容无法修改的列表',
    'dictionary':'字典，用来存储键值对',
}
for k,v in vocabulary.items():
    print(f'在Python中，“{k}”的含义是{v}!')
for k in vocabulary.keys():
    print(k)
for v in vocabulary.values():
    print(v)