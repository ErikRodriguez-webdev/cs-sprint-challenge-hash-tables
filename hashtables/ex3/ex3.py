def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # set cache to empty dictionary
    cache = {}

    # set results to list to catch intersection
    result = []

    # set num_exist_num_list to length of arrays
    num_exist_num_list = len(arrays)

    # for loop through array of arrays
    for array in arrays:
        # for loop through num of array
        for num in array:
            # check if num is in dictionary
            if num in cache:
                # then add one to cache[num] count
                cache[num] += 1
            else:
                # create a key with cache[num] starting at 1
                cache[num] = 1

    # for loop through all key and values stored in cache
    for pair in cache.items():
        # check if counter value tracks is equal to number of each list to exist
        if pair[1] == num_exist_num_list:
            # then add only key to results array
            result.append(pair[0])

    return result

# if __name__ == "__main__":
#     arrays = []

#     arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
#     arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
#     arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

#     print(intersection(arrays))
