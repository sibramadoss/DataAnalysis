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

print(red[7] == red[8] - 1)
print(red[7])
print(range(0,len(red)-1))

ctr = 0
for index in range(0,len(red)-1):
    if red[index] != red[index + 1] - 1:
        ctr = 0
        continue
    elif red[index] == red[index+1] -1 : 
        ctr = ctr + 1
        if ctr == 6:
            print(index - 6)
            break
        continue
print(ctr)






