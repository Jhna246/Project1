def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] > pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return(i+1)


def quickSort(arr, low, high):
    if low < high:
        pIndex = partition(arr, low, high)

        quickSort(arr, low, pIndex - 1)
        quickSort(arr, pIndex + 1, high)


arr = [1, 5, 3, 4, 2, 7, 6, 9, 10, 8]
n = len(arr)
quickSort(arr, 0, n-1)
print(arr)