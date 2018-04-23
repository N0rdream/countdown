import pytz
from datetime import datetime
from .helpers import add_zero


def get_countdown(date_event):
    dt_event = datetime.strptime(date_event, '%d.%m.%Y %H:%M')
    msk_tz = pytz.timezone('Europe/Moscow')
    dt_event_tz = msk_tz.localize(dt_event)
    dt_now_tz = datetime.now(tz=pytz.UTC)
    countdown = dt_event_tz - dt_now_tz
    total_secs = countdown.seconds
    if total_secs >= 0:
        nums = countdown.days, total_secs // 3600, total_secs // 60 % 60
        return [add_zero(num) for num in nums]
    return ('00', '00', '00')