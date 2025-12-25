words = []
new_words = []
while True:
    kiriting = input("So'z kiriting.(To'xtash uchun stopni bosing!): ")
    words.append(kiriting)

    if kiriting == "stop":
        break
    if len(kiriting) >= 5:
        new_words.append(kiriting)

print("List1 = ", words)
print("List2 = ", new_words)    
