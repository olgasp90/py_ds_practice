def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    count = 0
    for p in parens:
        if p == '(':
            count += 1
        elif p == ')':
            count -= 1
        # if parens start with a closing parenthese or
        # there are too many right parens the test fails right away:
        if count < 0:
            return False
    return count == 0


print(valid_parentheses(")()("))
print(valid_parentheses("())"))
print(valid_parentheses("(()())"))
