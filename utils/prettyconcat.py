def pretty_concat(strings, single_suffix='', multi_suffix=''):
    """Concatenates things in a pretty way"""
    if len(strings) == 1:
        return strings[0] + single_suffix
    elif len(strings) == 2:
        return '{} and {}{}'.format(*strings, multi_suffix)
    else:
        return '{}, and {}{}'.format(', '.join(strings[:-1]), strings[-1], multi_suffix)