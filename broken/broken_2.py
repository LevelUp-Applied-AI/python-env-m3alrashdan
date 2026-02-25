def get_length(text):
    """
    Returns the length of the given text.
    """
    return len(text)


# Intentional bug: passing None instead of a string
value = 'test'
result = get_length(value)
print("Length:", result)