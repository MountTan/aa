def quick_sort(alist, start, end):
    # 递归结束条件
    if start >= end:
        return

    # 设置基准元素
    mid = alist[start]

    # 设置从左往右的游标
    low = start

    # 设置从右往左的游标
    high = end

    while low < high:
        while low < high and alist[high] >= mid:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < mid:
            low += 1
        alist[high] = alist[low]

    alist[low] = mid

    quick_sort(alist, low + 1, end)

    quick_sort(alist, start, low - 1)


alist = [23, 1, 45, 20, 5, -8, 93, 10, 23]
quick_sort(alist, 0, len(alist)-1)
print(alist)


