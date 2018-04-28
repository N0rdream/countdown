from countdown.helpers import get_words


def test_get_words():
    assert get_words(('01', '03', '07')) == ['день', 'часа', 'минут']
    assert get_words(('03', '07', '01')) == ['дня', 'часов', 'минута']
    assert get_words(('77', '71', '73')) == ['дней', 'час', 'минуты']
    assert get_words(('10', '21', '12')) == ['дней', 'час', 'минут']
    assert get_words(('33', '14', '15')) == ['дня', 'часов', 'минут']
    assert get_words(('13', '12', '41')) == ['дней', 'часов', 'минута']