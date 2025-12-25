words = []
long_word = ""

while True:
    word = input("So'z kiriting(To'xtatish uchun stop yozing!) ")
    
    if word == 'stop':
        break

    if len(word) > len(long_word):
        long_word = word

print("Ro'yxatdagi eng uzun so'z: ", long_word)        

