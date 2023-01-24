def merge_sort(l):
    if len(l) < 2:
        return l

    mid_index = len(l)//2
    left = l[:mid_index]
    right = l[mid_index:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    sorted_list = []
    current_index_left = 0
    current_index_right = 0

    while len(sorted_list) < len(left) + len(right):
        if((current_index_left < len(left)) and (current_index_right == len(right) or sorted_left[current_index_left] < sorted_right[current_index_right])):
            sorted_list.append(sorted_left[current_index_left])
            current_index_left += 1
        else:
            sorted_list.append(sorted_right[current_index_right])
            current_index_right += 1

    return sorted_list
"""
time complexity: O(nlog n)
"""

l = [2, 1, 7, 6, 4, 3, 9]
print(merge_sort(l))
