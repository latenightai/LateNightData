def binary_search(target, nums):
    """
    we think of floor_index and ceiling_index as walls around
    the possible positions of our target so by -1 
    below we mean to start our wall to "To the left of the 0th index.    
    """
    floor_index = -1
    ceiling_index = len(nums)

    while(floor_index + 1 < ceiling_index):
        distance = ceiling_index - floor_index
        half_distance = distance // 2
        guess_index = floor_index + half_distance
        guess_value = nums[guess_index]

        if guess_value == target:
            return True

        if guess_value > target:
            # target is to the left, so move ceiling to the left
            ceiling_index = guess_index

        else:
            # target is to the right, so move floor to the right
            floor_index = guess_index
    return False


l = [1, 2, 3, 4, 5, 5, 6]
k = 9
print(binary_search(k, l))


"""
Divide the original list of size(n) in half untill we get down to 1

n * 1/2 * 1/2 ... = 1
n * (1/2)^x = 1
n/2^x = 1
n = 2^x
log n = log 2^x
log n = x

so the time complexity of the binary search is O(log n)
"""
