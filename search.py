# 顺序遍历查找算法
def seq_search(arr, key):
    sum = len(arr)
    for i in range(sum):
        if arr[i] == key:
            return i
    return None


# 二分查找算法
def binary_search(arr, low, heigh, key):
    if low <= heigh:
        mid = int(low + (heigh - low) / 2)
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search(arr, low, mid - 1, key)
        else:
            return binary_search(arr, mid + 1, heigh, key)
    else:
        return None


# 插值查找算法
def interpolation_search(arr, low, heigh, key):
    if low < heigh:
        interpolation = int((key - arr[low]) / (arr[heigh] - arr[low])\
             * (heigh - low)) + low
        if arr[interpolation] == key:
            return interpolation
        elif arr[interpolation] > key:
            return interpolation_search(arr, low, interpolation - 1, key)
        else:
            return interpolation_search(arr, interpolation + 1, heigh, key)
    elif low == heigh:
        if arr[low] == key:
            return low
        else:
            return None
    return None


# 测试代码
arr = [6, 7, 15, 3, 4, 9, 71, 21, 0, 8, 19]
print("sequential search:")
print(seq_search(arr, 0))
print(seq_search(arr, 10))

arr = [1, 3, 7, 9, 10, 19, 21, 31, 40, 88]
print("binary search:")
print(binary_search(arr, 0, len(arr) - 1, 10))
print(binary_search(arr, 0, len(arr) - 1, 0))


arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print("interpolation search:")
print(interpolation_search(arr, 0, len(arr) - 1, 7))
print(interpolation_search(arr, 0, len(arr) - 1, 12))
