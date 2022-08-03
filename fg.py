SolutionArr = []
arr711 = []
currentMax = 0
i,j = 0,0

for i in range(0,100):
    arr711.append(i* 7)
    arr711.append(i * 11)

sumHolder = []
counter = 0
i,j = 0,0
while len(sumHolder) < 101:
    if counter % 3 == 0:
        sum = 0
        i += 1
        sum = i*7 + j*11
        sumHolder.append(sum)        
    elif counter % 3 == 1:
        sum = 0
        i -= 1
        j += 1
        sum = i*7 + j*11
        sumHolder.append(sum)        
    else:
        sum = 0
        i += 1
        sum = i*7 + j*11
        sumHolder.append(sum)        

    counter +=1


for i in arr711:
    if i == 0:
        arr711.remove(i)

SolutionArr.append(0)
while len(SolutionArr) < 101:
    tempMin_711 = min(arr711)
    tempMin_Combo = min(sumHolder)
   
    if tempMin_711 < tempMin_Combo:
        if tempMin_711 in SolutionArr:
            arr711.remove(tempMin_711)
            continue
        else:
            SolutionArr.append(tempMin_711)
            arr711.remove((tempMin_711))
       
    elif tempMin_711 > tempMin_Combo:
        if tempMin_Combo in SolutionArr:
            sumHolder.remove(tempMin_Combo)
            continue
        else:
            SolutionArr.append(tempMin_Combo)
            sumHolder.remove(min(sumHolder))
   
    else:
        SolutionArr.append(tempMin_711)
        arr711.remove((tempMin_711))
#print(SolutionArr)


red = [0, 2, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 18, 20]


print(len(red) - 7)
print(range(0,7))


#I need to compare index x to index x+5
#len(red) - 5 will put me at 5 places before my list ends
#that means I will have 1 --> len(red) - 5 numbers or up to 0 --> len(red) - 6 index
#I need the indexes so I need 0 --> len(red) - 6 indexes
#len(red) - 5 > len(red) - 6
#range function gives you from 0 to x-1
#Im working with indices so I need 0 --> len(red)-6
#so range will be from 0 --> (len(red) - 5) - 1


print(len(red))
print(range(0,len(red) - 5))

for index in range(0, len(red) - 5):
    if red[index] != red[index + 5] - 5:
        continue
    elif red[index] == red[index + 5] - 5:
        print(index)
        continue
    else:
        continue







