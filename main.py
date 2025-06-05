import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

sizes = [100, 1000, 5000]

for size in sizes:
    print(f"\n=== Тестування для списку розміру {size} ===")

    arr = [random.randint(0, size) for _ in range(size)]

    arr_copy1 = arr[:]
    start = time.time()
    insertion_sort(arr_copy1)
    time_insertion = time.time() - start

    arr_copy2 = arr[:]
    start = time.time()
    merge_sort(arr_copy2)
    time_merge = time.time() - start

    arr_copy3 = arr[:]
    start = time.time()
    sorted(arr_copy3)
    time_timsort = time.time() - start

    print(f"Сортування вставками: {time_insertion:.6f} сек")
    print(f"Сортування злиттям : {time_merge:.6f} сек")
    print(f"Timsort (sorted)   : {time_timsort:.6f} сек")
