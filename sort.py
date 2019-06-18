import copy

arr = [4, 7, 8, 11, 4, 6, 13, 0, 9, 2]


# 冒泡排序
# 从无序序列头部开始，进行两两比较，根据大小交换位置，
# 直到最后将最大（小）的数据元素交换到了无序队列的队尾，
# 从而成为有序序列的一部分；
# 下一次继续这个过程，直到所有数据元素都排好序
def bubble_sort(arr):
    sum = len(arr)
    for i in range(sum - 1):
        for j in range(sum - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp
    return arr


# 选择排序
# 每一趟从待排序的记录中选出最小的元素，
# 顺序放在已排好序的序列最后，直到全部记录排序完毕
def selection_sort(arr):
    sum = len(arr)
    for i in range(sum):
        min = i
        for j in range(i, sum):
            if arr[j] < arr[min]:
                min = j
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp
    return arr


# 插入排序
# 每次将一个待排序的元素与有序序列的元素进行逐一比较，
# 直到找到合适的位置按大小插入
def insertion_sort(arr):
    sum = len(arr)
    for i in range(1, sum):
        target = arr[i]
        j = i
        while j > 0 and arr[j - 1] > target:
            arr[j] = arr[j - 1]
            j = j - 1
        arr[j] = target
    return arr


# 快速排序
# 基于分而治之的思想
# 首先选择列表中的一个元素作为基准元素，其他的元素都与这个元素做比较，
# 找出小于这个基准值的值、大于基准值的值
# 然后再将“小于v”和“大于v”的数据块作为子数组，
# 同样选择基准值，再进行上述类似操作，
# 当执行到数据块中只有1个元素或者0个元素时，即完成排序。
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


# 希尔排序
def shell_sort(arr):
    return arr


# 归并排序
def merge_sort(arr):
    return arr


# 堆排序
def heap_sort(arr):
    return arr


print("bubble sort:")
print(bubble_sort(copy.copy(arr)))

print("selection sort:")
print(selection_sort(copy.copy(arr)))

print("insertion sort:")
print(insertion_sort(copy.copy(arr)))

print("quick sort:")
print(quick_sort(copy.copy(arr)))

print("shell sort:")
print(shell_sort(copy.copy(arr)))

print("merge sort:")
print(merge_sort(copy.copy(arr)))

print("heap sort:")
print(heap_sort(copy.copy(arr)))
