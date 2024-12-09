import time

# Helper function to print arrays
def print_array(arr):
    print(" ".join(map(str, arr)))

# Bubble Sort algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
                swapped = True
        if not swapped:
            break

# Merge Sort algorithm
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
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Quick Sort algorithm
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = [el for el in arr[:-1] if el <= pivot]
    right = [el for el in arr[:-1] if el > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

# Insertion Sort algorithm
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Main Program
original_array = [5, 2, 8, 4, 1, 9, 7]

print("Original Array:")
print_array(original_array)

# Bubble Sort
bubble_sorted_array = original_array[:]
start_time = time.time()
bubble_sort(bubble_sorted_array)
end_time = time.time()
print(f"Bubble Sort Time: {end_time - start_time:.6f} seconds")
print("Array Sorted Using Bubble Sort:")
print_array(bubble_sorted_array)

# Merge Sort
merge_sorted_array = original_array[:]
start_time = time.time()
merge_sorted_array = merge_sort(merge_sorted_array)
end_time = time.time()
print(f"Merge Sort Time: {end_time - start_time:.6f} seconds")
print("Array Sorted Using Merge Sort:")
print_array(merge_sorted_array)

# Quick Sort
quick_sorted_array = original_array[:]
start_time = time.time()
quick_sorted_array = quick_sort(quick_sorted_array)
end_time = time.time()
print(f"Quick Sort Time: {end_time - start_time:.6f} seconds")
print("Array Sorted Using Quick Sort:")
print_array(quick_sorted_array)

# Insertion Sort
insertion_sorted_array = original_array[:]
start_time = time.time()
insertion_sort(insertion_sorted_array)
end_time = time.time()
print(f"Insertion Sort Time: {end_time - start_time:.6f} seconds")
print("Array Sorted Using Insertion Sort:")
print_array(insertion_sorted_array)
