alist=[]
try:
    with open('D:/Sruthi/Learning/Python Learning/animal.txt') as text:
        i=0
        for line in text:
            alist=text.readlines()
            i+=1
        sorted_animals=sorted(alist)
        print(sorted_animals)
    
except:
    print("'File doesn't exist")

with open('D:/Sruthi/Learning/Python Learning/animal_sorted.txt','x') as text1:
    for items in sorted_animals:
        text1.write(items)

