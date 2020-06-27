def heading(string, head=1):
    n_hash = head
    if n_hash < 1:
        n_hash = 1
    elif n_hash > 6:
        n_hash = 6
    return '#' * n_hash + ' ' + string