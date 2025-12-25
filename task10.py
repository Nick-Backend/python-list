names = ['Ozod', 'Diyor', 'Sherzod']

index = int(input('Indeksni kiriting: '))
new_value = input('Yangi qiymatni kiriting: ')

names.pop(index)
names.insert(index, new_value)

print(names)