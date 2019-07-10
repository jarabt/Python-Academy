def all(seq):
    for item in seq:
        if not item:
            return False
    return True

def any(seq):
    for item in seq:
        if item:
            return True
    return False


print(any([0, 0, "s"]))
