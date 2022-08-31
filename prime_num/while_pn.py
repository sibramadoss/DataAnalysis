i = 0
pnlist = []

while i >= 0:
    if i == 0 or i == 1:
        i += 1
        continue
    else:
        for j in range(2, (i//2)+1):
            if i % j == 0:
                break
        else:
            pnlist.append(i)
            if len(pnlist) == 20:
                break
                #for else syntax --> the else block only executes if the for loop above does not break
                #if the statement does break it skips to the i += 1 line and goes back to the while
                #if the statement breaks it goes to pnlist.append and then checks is list == 20 
                #if it satisfies it breaks out of the entroe while loop now
        i += 1

print(pnlist)

