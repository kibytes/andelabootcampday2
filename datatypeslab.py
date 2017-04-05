def data_type(d):
    if isinstance(d, bool):
        return d
    elif isinstance(d, str):
        return len(d)
    elif isinstance(d, int):
        if d < 100:
            return 'less than 100'
        elif d > 100:
            return 'more than 100'
        else:
            return 'equal to 100'
    elif isinstance(d, list):
        try:
            return d[2]
        except IndexError:
            return None
    else:
        return 'no value'

