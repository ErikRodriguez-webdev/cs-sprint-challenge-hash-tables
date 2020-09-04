def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # set result to empty list
    result = []

    # set cache to empty dictionary
    cache = {}

    # for loop through range length parameter
    for i in range(length):
        difference = limit - weights[i]
        # check if difference is in cache with limit minus current index value
        if difference in cache:
            # append both indices to result list
            result.append(i)
            result.append(cache[difference])
            # return result list with indices
            return result
        # else
        else:
            # store in cache for later use
            cache[weights[i]] = i

    # return none if nothing found
    return None


print(get_indices_of_item_weights([4, 4], 2, 8))
