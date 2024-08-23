dist=int(input('Enter the distance you want to travel: '))
if dist<3:
    print('I suggest you to walk to your destination')
elif dist<300:
    print('I suggest you to drive to your destination')
else:
    print('I suggest you to fly to your destination')