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
        #setting up dictionary with source as key, destination as value
        dict[x.source] = x.destination
    
    next = dict["NONE"]
    routeCache.append(next)

    for x in range(0, length):
        # find next destination by using previous ticket's destination as key for source
        next = dict[next]
        routeCache.append(next)
        # Why someone would have a ticket with no destination is unclear, but when they do 
        # next == NONE, so:
        if next == "NONE":
            break

    return routeCache
            


