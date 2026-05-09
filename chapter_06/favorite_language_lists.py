favorite_languages = {
    'jen':['python','rust'],
    'sarah':['C'],
    'edward':['rust','go'],
    'phil':['python','haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages)==1 :
        print(f"\n{name}'s favorite language is {languages[0]}.")
    else:
        print(f"\n{name.title()}'s favorite languages are:")

        for language in languages:
            print(f"\t{language.title()}")