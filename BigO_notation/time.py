# O(1)
def print_first_item(items):
    print(items[0])

# O(n)
def print_all_items(items):
    for item in items:
        print(item)

# O(n^2)
def print_all_possible_ordered_pairs(items):
    for first_item in items:
        for second_item in items:
            print(first_item, second_item)


print_all_possible_ordered_pairs([1, 2, 3, 4])
