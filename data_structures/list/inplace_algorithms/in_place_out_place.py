def square_list_in_place(int_list):
    for index, element in enumerate(int_list):
        int_list[index] *= element

    # we modified int_list in place

def square_list_out_of_place(int_list):
    squared_list = [None] * len(int_list)

    for index, element in enumerate(int_list):
        # we allocate a new list with the length of the input list
        squared_list[index] = element ** 2
    
    return squared_list


print(square_list_in_place([1, 2, 3, 4, 5]))

print(square_list_out_of_place([1, 2, 3, 4, 5]))