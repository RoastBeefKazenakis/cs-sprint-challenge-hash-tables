def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}

    # cache the weights/indices. Key: weight, value: index
    for x in range(length):
        cache[weights[x]] = x
    
    # perform subtraction operation, check cache for result. if result in cache ->
    for y in range(length):
        diff = limit - weights[y]
    # we found two indices to add which will equal limit, output them using max and min with the weights as keys
        if diff in cache:
            return(max(y, cache[diff]), min(y, cache[diff]))
    return None

