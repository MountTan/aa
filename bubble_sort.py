def bubble_sort(alist):
    for i in range(len(alist) - 1, 0, -1):
        for j in range(i):
            if alist[j] >= alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]


alist = [1, 3, 7, 20, 7, 5, 5, 18, 10, ]
bubble_sort(alist)
print(alist)
