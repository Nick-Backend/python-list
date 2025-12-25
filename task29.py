numbers = []

for number in range(10):
    number = int(input("Enter number: "))
    numbers.append(number)

print("Kirititlgan sonlar:",numbers)  

takrorlanmas = []

for number in numbers:
    if numbers.count(number) == 1:
        takrorlanmas.append(number)

print("Takrorlanmagan sonlar:", takrorlanmas)        