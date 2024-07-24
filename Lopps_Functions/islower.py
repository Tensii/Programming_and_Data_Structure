def islower(c):
    if len(c) != 1:
        return False
    ascii_value = ord(c)
    if 97 <= ascii_value <= 122:
        return True
    return False
