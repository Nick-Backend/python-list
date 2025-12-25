list_3kichik = []
list_6kichik = []
list_6katta = []

while True:
    enter_word = input("So'z kiriting(To'xtatish uchun stop kiriting!) ")
    if enter_word == 'stop':
        break

    if len(enter_word) <= 3:
        list_3kichik.append(enter_word)

    elif len(enter_word) <= 6:
        list_6kichik.append(enter_word) 

    else:
        list_6katta.append(enter_word)


print("Uzunligi <= 3 elementli ro'yxat ", list_3kichik)  
print("Uzunligi <= 6 elementli ro'yxat ", list_6kichik) 
print("Uzunligi > 6 elementli ro'yxat ", list_6katta)   

