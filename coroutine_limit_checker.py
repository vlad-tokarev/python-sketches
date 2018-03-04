from collections import defaultdict
from itertools import cycle


def limit_checker(max_, start_count=0):
    """
    Simple coroutine based checker that count occurrences by different keys (str) and return info limit reached or not
    :param max_: max_ limit occurrences for each key
    :param start_count: start state of counter while it created first time for key
    :return: True if limit by key is reached and False if not

    Use Cases: TODO: Add description of possible use cases for this checker

    Example:

    >>> check_limit = limit_checker(2)
    >>> check_limit("A")
    False
    >>> check_limit("B")
    False
    >>> check_limit("A") # Second occurrence while limit is two
    True
    """

    def updates_counter_fabric():
        counter = cycle(range(max_))

        # if start_count is not 0 then we need rewind counter to required position
        if start_count:
            while True:
                if next(counter) == start_count - 1:
                    break

        return counter

    counter_dict = defaultdict(updates_counter_fabric)

    pair = yield
    while True:
        count = next(counter_dict[pair])
        limit_reached = count == (max_ - 1)
        pair = yield limit_reached
