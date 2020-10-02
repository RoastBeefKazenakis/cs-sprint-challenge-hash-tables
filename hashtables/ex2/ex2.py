#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    dict = {}
    routeCache = []

    for x in tickets:
        dict[x.source] = x.destination
    
    next = dict["NONE"]
    routeCache.append(next)

    for y in range(0, length):
        next = dict[next]
        routeCache.append(next)
        if next == "NONE":
            break

    return routeCache
            


