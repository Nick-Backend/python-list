numbers = [1, 2, 3, 2, 2, 4, 5, 6]

max_count = 0
kup_son = None

for number in numbers:
    count = numbers.count(number)

    if count > max_count:
        max_count = count
        kup_son = number

print("Ko'p takrorlangan son:", kup_son)        