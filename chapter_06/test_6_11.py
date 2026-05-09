cities = {
    'Beijing':{
        'country':'China',
        'population':15000000,
        'fact':'It is the capital of China!',
    },
    'NewYork':{
        'country':'the USA',
        'population':20000000,
        'fact':'It is very rich!',
    },
    'Tokyo':{
        'country':'Japan',
        'population':6000000,
        'fact':'The people here eat fish a lot',
    },
}

for place, infos in cities.items():
    print(f"{place}'s info lists :")
    for key, value in infos.items():
        print(f"\t{key}:{value}")