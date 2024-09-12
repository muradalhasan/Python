my_list = [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]

def bubble_sort(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                # Swap the elements if they are in the wrong order
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

sorted_list = bubble_sort(my_list)
print("Sorted list:", sorted_list)
