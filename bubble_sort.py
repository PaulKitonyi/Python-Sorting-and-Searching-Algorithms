def bubble_sort(l):
    swap=False
    while not swap:
        print('bubble sort: ' +str(l))
        swap=True
        for j in range(1,len(l)):
            if l[j-1] > l[j]:
                swap=False
                temp=l[j]
                l[j]=l[j-1]
                l[j-1] = temp
                
'''For testing purpose'''
testlist=[21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40]
print('')
print(bubble_sort(testlist))
print(testlist)
