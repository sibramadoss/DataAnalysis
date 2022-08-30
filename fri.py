i = 0
pnlist = []

while i >= 0:
    if i == 0 or i == 1:
        i += 1
        continue
    else:
        for j in range(2, int(i/2)+1):
            if i % j == 0:
                break
        else:
            pnlist.append(i)
            if len(pnlist) == 20:
                break
        i += 1

print(pnlist)
