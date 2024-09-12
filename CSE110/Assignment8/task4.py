sitting_list = [10, 30, 20, 70, 11, 15, 22, 16, 58, 100, 12, 56, 70, 80]

def organize_sitting_list(lst):
    even_indices = [lst[i] for i in range(0, len(lst), 2)]
    odd_indices = [lst[i] for i in range(1, len(lst), 2)]
    even_indices.sort()
    odd_indices.sort(reverse=True)
    organized_list = []
    even_idx = 0
    odd_idx = 0
    for i in range(len(lst)):
        if i % 2 == 0:
            organized_list.append(even_indices[even_idx])
            even_idx += 1
        else:
            organized_list.append(odd_indices[odd_idx])
            odd_idx += 1

    return organized_list
organized_sitting_list = organize_sitting_list(sitting_list)
print("Organized sitting arrangement:", organized_sitting_list)
