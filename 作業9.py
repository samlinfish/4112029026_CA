#Some of my codes are done by ChatGpt, but I made sure to thoroughly
#understand the code, except merge sort. I really don't understand merge sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    #Seperating the array into three parts
    left = [x for x in arr if x < pivot] 
    middle = [x for x in arr if x == pivot] 
    right = [x for x in arr if x > pivot]
    #Continues to process two subarrays until they have one element left
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort the left and right halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    sorted_arr = []
    left_index = right_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            sorted_arr.append(left_half[left_index])
            left_index += 1
        else:
            sorted_arr.append(right_half[right_index])
            right_index += 1

    # Append the remaining elements, if any
    sorted_arr.extend(left_half[left_index:])
    sorted_arr.extend(right_half[right_index:])

    return sorted_arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        #無需考慮最後i個，因為我們已經確認最後i個數就是最大的
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
        #看key的前面一格有沒有比key大，如果有，那格的值就往右複製，
        #然後往前再比，比到最後迴圈條件不滿足，key的值就會跳到第一個位置或是
        #最後一個往右複製的那格
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def main():
    input_array = [5, 4, 1, 8, 2, 6]
    
    print("Quick Sort:", quick_sort(input_array))
    print("Depends on whether or not the pivot divides the substrings evenly.\n")

    print("Merge Sort:", merge_sort(input_array))
    print("There's no worst case and best case for merge sort\n")

    print("Bubble Sort:", bubble_sort(input_array))
    print("Worst case: [8,6,5,4,2,1] Best case: [1,2,4,5,6,8]\n")

    print("Insertion Sort:", insertion_sort(input_array))
    print("Worst case: [8,6,5,4,2,1] Best case: [1,2,4,5,6,8]\n")

main()
