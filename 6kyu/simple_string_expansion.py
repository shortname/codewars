import re

def string_expansion(s):
    def repl(obj):
        return int(obj.group(1))*obj.group(2)
    result = '1' + s if len(s) > 0 else s
    result = re.sub(r'\d+(\d)', r'\1', result)
    result = re.sub(r'\d$', '', result)
    subs = None
    while subs != 0:
        result, subs = re.subn(r'(\d)([A-Za-z])([A-Za-z])', r'\1\2\1\3', result)
    return re.sub('(\d)([A-Za-z])', repl, result)