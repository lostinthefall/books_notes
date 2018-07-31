# coding=utf-8
# 《算法图解：像漫画小说一样有趣》.pdf

###

# P19 二分查找
# 接受一个有序数组和一个元素
def binary_search(list_a, item):
    low_index = 0
    high_index = len(list_a) - 1
    while low_index <= high_index:
        mid_index = (low_index + high_index) / 2
        mid_num = list_a[mid_index]
        if mid_num == item:
            return mid_index
        if mid_num > item:
            high_index = mid_index - 1
        else:
            low_index = mid_index + 1
    return None


# list 需要按顺序排列
list_a = [1, 2, 3, 4, 5, 6, 45, 67, 78, 89, 245]


# print binary_search(list_a, 6)


###

# P28 选择排序
def findSmallestItem(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(0, len(arr)):
        index = findSmallestItem(arr)
        newArr.append(arr.pop(index))
    return newArr


# P47
def add(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        x = arr.pop(0)
        print arr
        return x + add(arr)


# P52
def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        # 挑出一个数组除第一个以外比num小的数字放到一个列表里
        # - https://developers.google.com/edu/python/sorting List Comprehensions (optional)
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)


if __name__ == '__main__':
    # print add([1, 2, 3, 4, 5])

    print quickSort([2, 5, 1, 87, 33, 26])
