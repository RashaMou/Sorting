# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        # set the current index at 0
        smallest_index = cur_index
        # inner loop finds the smallest element by looping through everything to the right of the current index and comparing each element with the element that is currently in the smallest index. If the element is smaller, then we set that to the smallest index.
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # Once we've found the index of the smallest element, we then set the current index to the index of the smallest element and then repeat the loop n-1 times.
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr


print(selection_sort([3, 2, 1, 12, 7, 4, 6, 1, 2, 0]))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for _ in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


# print(bubble_sort([3, 2, 1, 12, 7, 4, 6, 1, 2, 0]))

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):
    pass
    return arr

