def selection_sort(l):
    suffixst=0
    while suffixst != len(l):
        print('selection sort: ' + str(l))
        for i in range(suffixst, len(l)):
            if l[i] < l[suffixst]:
                l[suffixst], l[i] = l[i],l[suffixst]
        suffixst += 1

'''For testing purposes'''
testlist= [21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40]
print('')
print(selection_sort(testlist))
print(testlist)
