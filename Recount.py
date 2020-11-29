import sys

def findMax(names):
    max = -999
    runoff = 0
    person = str()
    for name in names:
        if names[name] > max:
            person = name
            max = names[name]
    for name in names:
        if names[name] == max:
            runoff += 1
    return person if runoff < 2 else 'Runoff!'

def process(names, name):
    if name in names:
        names[name] += 1
    else:
        names[name] = 1
    return names

done = False
names = dict()
while(done == False):

    name = input()
    process(names, name)
    if name == "***":
        done = True
winner = findMax(names)

print(winner)
    