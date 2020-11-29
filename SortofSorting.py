import sys

 
def sortOfSort(names):
    sorted = []
    for i in range(len(names)-1):
        for k in range(len(names)-i- 1):
            if names[k][0] > names[k+1][0]:
                temp = names[k]
                names[k] = names[k+1]
                names[k+1] = temp
            elif names[k][0] == names[k+1][0]:
                if names[k][1] > names[k+1][1]:
                    temp = names[k]
                    names[k] = names[k+1]
                    names[k+1] = temp
    return names

cases = int(input())
while(cases != 0):
    names = []
    for i in range(cases):
        names.append(str(input()))
    sortOfSort(names)
    cases = int(input())
    for name in names:
        print(name)
    print('')

