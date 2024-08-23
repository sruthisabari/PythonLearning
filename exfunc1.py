def fillstory(noun, verb, adj):
    story='{0} {1} {2} girl. She {1} very intelligent. Everyone likes {0}.'.format(noun, verb,adj)
    return story
def getdata():
    noun=input('Enter a noun:')
    verb=input('Enter a verb: ')
    adj=input('Enter an adjective: ')
    story=fillstory(noun,verb,adj)
    return story

def get_and_tellstory():
    story=getdata()
    print(story)

get_and_tellstory()