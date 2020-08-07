def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # set cache to empty dictionary
    cache = {}

    # set result to list to catch pos / neg pair
    result = []

    # for loop through num of a
    for num in a:
        # remove symbol from num with absolute value method
        new_num = abs(num)
        # check if new_num in dictionary
        if new_num in cache:
            # then add one to cache[new_num]
            cache[new_num] += 1
        else:
            # create a key cache[num] set to 1
            cache[new_num] = 1

    # for loop through pair of cache.items()
    for pair in cache.items():
        # check if pair[1] is equal to two
        if pair[1] == 2:
            # then append only the key to result list
            result.append(pair[0])

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
