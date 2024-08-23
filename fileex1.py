try:
    with open('D:/Sruthi/Learning/Python Learning/file1.txt') as text:
        i=1
        for line in text:
            print('{}: {}'.format(i,line.rstrip()))
            i+=1
except:
    print("'File doesn't exist")

