mydict={'jeff':'Is afraid of clowns','David':'Plays the piano','Jason':'Can fly an airplane'}

for item in mydict:
    print('{}: {}'.format(item,mydict[item]))

mydict['jeff']='Is afraid of heights'
mydict['Jill']='Can hula dance.'

print('new dictionary is: ')

for item in mydict:
    print('{}: {}'.format(item,mydict[item]))