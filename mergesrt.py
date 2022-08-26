def mrge(array):
    if len(array) > 1:
        la = array[:len(array)/2]
        ra = array[len(array)/2:]

        # recursion
        mrge(la)
        mrge(ra)

        # merge

        i , j = 0 , 0
        k = 0

        while i < len(la) and j<len(ra):
            if la[i] < ra[j]:
                array[k] = la[i]
                i += 1
            else:
                array[k] = ra[j]
                j += 1
            k += 1
        
        while i<len(la):
            array[k] = la[i]
            i += 1
            k += 1
        
        while j<len(ra):
            array[k] = ra[j]
            j += 1
            k += 1

        

if __name__ == '__main__':
    folly = [0,3,4,5,2,1]
    mrge(folly)
    # doesn't return anything so you have to print back the original array
    print(folly)
