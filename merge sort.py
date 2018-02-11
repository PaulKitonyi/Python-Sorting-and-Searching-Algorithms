def merge(left,right):
    result=[]
    i,j=0,0
    while (i < len(left) and j < len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while (i < len(left)):
        result.append(left[i])
        i += 1

    while(j < len(right)):
        result.append(right[j])
        j += 1
        print('merge: ' + str(left) + '&' + str(right))
    return result

def merge_sort(l):
    print('merge sort: ' + str(l))
    if len(l) < 2:
        return l[:]
    else:
        middle=len(l)//2
        left=merge_sort(l[:middle])
        right=merge_sort(l[middle:])
        return merge(left,right)

'''For testing purpose'''

testlist=[21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40]
print('')
print(merge_sort(testlist))

