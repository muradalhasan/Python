my_list = [4, 2, 3, 1, 6, 5]


def bubble_sort(lst):
    n = len(lst)
    count=0
    for i in range(n-1):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                count+=1
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return count

sorted_list = bubble_sort(my_list)
print("Sorted list:", sorted_list)
