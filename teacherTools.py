import random

#things to build?
#   seating chart
#   exporting stuff
#   random exam simulator
#       input could be a vector of number of options


groups = []


#takes a list of (students) and assigns them to groups
##def randomizeGroups(los, numBins):
##    random.shuffle(los)
##    groupLen = 
##
##    c = numBins
##    for i in groups:

def makeRandLst(sze):
    lst = []
    while sze > 0:
        lst.append(str(sze))
        sze = sze - 1
    return lst


#Yield n-sized chunks from l.
def chunks(l, n):
    if (len(l) % n) != 0:
        print("unequal Groups!")
    lst = []
    for i in range(0, len(l), n):
        lst.append(l[i:i + n])
    return lst

def randTopics(grps):
        
l = makeRandLst(10)
z = chunks(l, 3)
print(z)
l.pop()
z = chunks(l, 3)
print(z)










