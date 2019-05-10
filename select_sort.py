def select_sort(alist):
    n = len(alist)

    for i in range(n - 1):

        min_index = i
        for j in range(i + 1, n):
            if alist[j] < alist[min_index]:
                min_index = j

        if i != min_index:
            alist[i], alist[min_index] = alist[min_index], alist[i]


alist = [22, 6, 8, 3, 50, -5, 74, 2]
select_sort(alist)
print(alist)
