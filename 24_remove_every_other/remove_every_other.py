def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    result = []
    for item in lst:
        if lst.index(item) == 0:
            result.append(item)
        elif lst.index(item) % 2 == 0:
            result.append(item)
        else:
            pass
    print(lst)
    return result



lst = [1, 2, 3, 4, 5]
print(remove_every_other(lst))
