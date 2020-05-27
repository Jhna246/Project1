def mergeSort(arr):
    if len(arr) > 1:
        midpoint = len(arr) // 2
        l = arr[:midpoint]
        r = arr[midpoint:]
        print(l)
        print(r)

        mergeSort(l)
        mergeSort(r)

        i, j, k = 0, 0, 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1

arr = [1, 2, 5, 4, 10, 8, 7, 6]
mergeSort(arr)
print(arr)


