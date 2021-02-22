def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    to_swap = to_swap.lower()
    result = ''
    for letter in phrase:
        if letter.lower() == to_swap:
            letter = letter.swapcase()
        result += letter
    return result
print(flip_case('Aaaahhh', 'a'))
print(flip_case('Aaaahhh', 'A'))
print(flip_case('Aaaahhh', 'h'))

# letter != to_swap:



# my failed attempt:

#   result = ''
#    for letter in phrase:
#         # print(letter)
#         if letter == to_swap:
#             print(letter)
#             if letter.islower():
#                 print(letter)
#                 result += letter.upper()
#             else:
#                 print(letter)
#                 result += letter.lower()
#         else:
#             print(letter)
#             result += letter
#     return result
