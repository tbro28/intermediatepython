def parse(txt):
    """
    Return a list of integers from the string

    >>> parse('1,3,5,9')
    [1, 3, 5, 9]
    
    """
    results = []
    for item in txt.split(','):
        results.append(int(item))
    return results
