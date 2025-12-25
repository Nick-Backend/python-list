list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 5, 7, 8, 9, 10]
bir_xil = []

for i in list1:
    if i in list2 and i not in bir_xil:
        bir_xil.append(i)

print(bir_xil)        

