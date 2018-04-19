def add_zero(digit):
    if digit < 10:
        return '0' + str(digit)
    return str(digit)


def get_tuple(env_string):
    color = env_string.strip().replace(' ', '')
    return tuple(int(c) for c in color.split(','))