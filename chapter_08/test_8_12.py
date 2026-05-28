def make_sandwich(*foods):
    print('\n客人您刚点了：')
    for food in foods:
        print(f'\t - {food}')

make_sandwich('cheese')
make_sandwich('peppers','beef','bred')