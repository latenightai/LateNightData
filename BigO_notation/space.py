# O(1)
def say_hi_n_times(n):
    for time in range(n):
        print("hi")

# O(n)
def list_of_hi_n_items(n):
    hi_list = []
    for time in range(n):
        hi_list.append("hi")
    return hi_list

# Usually when we talk about space complexity, we're talking about additional space.
def get_largest_item(items):
    largest = float('-inf')
    for item in items:
        if item > largest:
            largest = item
    return largest


print(get_largest_item([1, 4, 6, 5, 2]))
