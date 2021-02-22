def frequency_count(collection):
    count = {}
    for item in collection:
        count[item] = count.get(item, 0) + 1
        print(count)
    return count

def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    return frequency_count(str(num1)) == frequency_count(str(num2))

print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))
print(same_frequency(1212, 2211))
