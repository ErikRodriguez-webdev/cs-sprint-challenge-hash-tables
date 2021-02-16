def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # set cache to empty dictionary
    cache = {}

    # set result to list to catch pos / neg pair
    result = []

    # sort list with positive numbers first and negative numbers last
    a = sorted(a, reverse=True)

    # for loop through a list
    for num in a:
        # check if num is negative and non negative num is in cache
        if num < 0 and abs(num) in cache:
            # then remove negative symbol with abs function
            new_num = abs(num)
            # add one to cache using key
            cache[new_num] += 1
        # check if num is positive
        elif num > 0:
            # then num is positive
            # store in cache with key as num and value as 1
            cache[num] = 1

    # for loop through cache dictionary
    for pair in reversed(cache.items()):
        # check if stored values are equal to 2
        if pair[1] == 2:
            # then append key to result list
            result.append(pair[0])

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
