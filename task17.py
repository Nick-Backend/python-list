names = []

while True:

    name = input("Ism kiriting.(To'xtash uchun stop kiriting: )")
    
    if name == 'stop':
        break

    names.append(name)

print("Jami ismlar", names)
print("Ismlar soni", len(names))        