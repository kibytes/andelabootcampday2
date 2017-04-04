def data_type(d):
    if isinstance(d, bool):
        return d
    elif isinstance(d, str):
        return (("String of length ") + str(len(d)))
    elif isinstance(d, int):
        if d < 100:
            return "integer less than 100"
        elif d > 100:
            return "integer more than 100"
        else:
            return "integer equal to 100"
    elif isinstance(d, list):
        try:
            return d[0]
        except IndexError:
            return "Empty List"
    else:
        return "no data given"

#print data_type("ght")
