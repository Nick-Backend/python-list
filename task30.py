words = ['alla', 'arra', 'ism', 'error', 'ikki']
palindroms = []

for word in words:
    if word == word[::-1]:
        palindroms.append(word)

print("Palindrome so'zlar:",palindroms)
