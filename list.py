mytodo=[]
flag=0
while flag==0:
    item=input('Please enter a to-do item:')
    if len(item)!=0:
        mytodo.append(item)
    else:
        flag=1
        
    
print('Your to do items are: ')
for i in mytodo:
    print(i)
    
    