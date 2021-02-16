#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    # set cache to empty dictionary
    cache = {}
    # set results to list to catch order of flights
    results = []

    # for loop ticket through tickets
    for ticket in tickets:
        # create a key(source flight) and value(destination flight)
        cache[ticket.source] = ticket.destination

    # set current_flight to starting point which will be NONE
    current_flight = "NONE"

    # while loop while True
    while True:
        # access cache key and append value into results list
        results.append(cache[current_flight])

        # redeclare current_flight to cache[current_flight] to next destination
        current_flight = cache[current_flight]

        # check if current_flight is equal to None
        if current_flight == "NONE":
            # then return results
            return results
