def to_weird_case(string):
    def set_case(char, index):
        return char.lower() if index % 2 else char.upper()
    separator = ' '
    words = string.split(separator)
    return separator.join([''.join([set_case(c, i) for i, c in enumerate(w)]) for w in words])