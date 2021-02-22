def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    reversed_phrase = phrase[::-1]
    return reversed_phrase


print(reverse_string('awesome'))
print(reverse_string('sauce'))
print(reverse_string('I am a student'))
