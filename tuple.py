mytuplelist=[('O’Hare International Airport','ORD'),('Los Angeles International Airport','LAX'),('Dallas/Fort Worth International Airport','DFW'),('Denver International Airport','DEN')]
for items in mytuplelist:
    (airport,code)=items
    print('The code for {} is {}'.format(airport,code))