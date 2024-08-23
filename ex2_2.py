costperhour=0.51
#oneserver
Costperday=costperhour*24
Costpermonth= costperhour*24*30
print('Cost of one server per day:{}'.format(Costperday))
print('Cost of one server per month:{}'.format(Costpermonth))
print('Cost of 20 server per day:{}'.format(Costperday*20))
print('Cost of 20 server per month:{}'.format(Costpermonth*20))
no=918/Costperday

print('no of days one server can operate with :{}'.format(int(no)))