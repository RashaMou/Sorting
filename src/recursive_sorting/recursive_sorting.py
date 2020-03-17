# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged = []
    # TO-DO
    index_a = index_b = 0
    # length of merged has to total the sum of the length of both arrays
    while len(merged) < elements:
        if arrA[index_a] <= arrB[index_b]:
            merged.append(arrA[index_a])
            index_a += 1
        else:
            merged.append(arrB[index_b])
            index_b += 1
        # if we reach the end of one of the arrays, we should break. Whenever we append, the index is incremented by 1, so when we append the last element, the index will be equal to len(arr), meaning we have reached the end
        if index_a == len(arrA):
            merged.append(arrB[index_b:])
        elif index_b == len(arrB):
            merged.append(arrA[index_a:])
    return merged


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    middle = len(arr) // 2
    lefthalf = arr[:middle]
    righthalf = arr[middle:]

    if len(lefthalf) == 1:
        print("lefthalf:", lefthalf)
        return lefthalf
    else:
        merge_sort(lefthalf)
    if len(righthalf) == 1:
        print("righthalf:", righthalf)
        return lefthalf
    else:
        merge_sort(righthalf)
    return arr


print(merge_sort([2, 6, 23, 67, 8, 2, 7, 8, 3, 45]))
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
