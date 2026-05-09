favorite_places = {
    'Alice':['Paris','Beijing','Ningxia'],
    'Dylan':['Hefei','Nanjing'],
    'Eris':['Hohhot','Xuzhou','Ninbo'],
}

for name, places in favorite_places.items():
    print(f"\n{name}'s favorite places are:")
    for place in places:
        print(f"\t{place}")
