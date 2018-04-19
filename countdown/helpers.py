def add_zero(digit):
    if digit < 10:
        return '0' + str(digit)
    return str(digit)


def get_tuple(env_string):
    color = env_string.strip().replace(' ', '')
    return tuple(int(c) for c in color.split(','))


def get_word(num, days=False, hours=False, minutes=False):
    if days:
        words = ('день', 'дня', 'дней')
    elif hours:
        words = ('час', 'часа', 'часов')
    elif minutes:
        words = ('минута', 'минуты', 'минут')
    last_digit = num[-1]
    if last_digit == '1':
        return words[0]
    if last_digit in ['2', '3', '4']:
        return words[1]
    return words[2]


def get_words(nums):
    return [
        get_word(nums[0], days=True),
        get_word(nums[1], hours=True),
        get_word(nums[2], minutes=True)]