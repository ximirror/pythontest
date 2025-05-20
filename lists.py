
def convert_to_list(_str: str) -> list:
    _list = []
    for char in _str:
        _list.append(char)
    return _list

def convert_to_string(_list: list) -> str:
    _str = ""
    for char in _list:
        _str += char
    return _str

def reverse_list(_list: list) -> list:
    reversed_list = []
    ## I don't know
    return reversed_list

if __name__ == "__main__":
    l = convert_to_list("Racecar")
    l2 = reverse_list(l)
    s = convert_to_string(l2)
    print(s)
