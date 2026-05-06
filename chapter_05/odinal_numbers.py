numbers = list(range(1,10))
odinal_numbers = []

for number in numbers:
    if(number==1):
        odinal_numbers.append('1st')
    elif(number==2):
        odinal_numbers.append('2nd')
    elif(number==3):
        odinal_numbers.append('3rd')
    else:
        odinal_numbers.append(f'{number}th')
print(odinal_numbers)