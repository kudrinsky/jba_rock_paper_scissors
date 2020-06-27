def get_percentage(number, precision=None):
    return f'{round(number * 100)}%' if precision is None else f'{round(number * 100, precision)}%'
