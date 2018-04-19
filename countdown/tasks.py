import os
import sys
import logging
from dotenv import load_dotenv
from .helpers import get_tuple
from .timer import get_countdown
from .vk_requests import get_upload_url, upload_file, save_cover
from .editors import create_cover
from celery import shared_task


@shared_task(ignore_result=True)
def update_cover():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MEDIA_DIR = os.path.join(BASE_DIR, 'media')
    load_dotenv(dotenv_path=os.path.join(BASE_DIR, '.env'))

    date_event = os.getenv('DATE_EVENT')
    cover_orginal_path = os.path.join(MEDIA_DIR, os.getenv('COVER_ORIGINAL_FILENAME'))
    cover_final_path = os.path.join(MEDIA_DIR, os.getenv('COVER_FINAL_FILENAME'))
    font_path = os.path.join(MEDIA_DIR, os.getenv('FONT_FILENAME'))
    color_rgb = get_tuple(os.getenv('COLOR'))
    color_size = int(os.getenv('COLOR_SIZE'))
    x_coords = get_tuple(os.getenv('X_COORDINATES'))
    y_coords = get_tuple(os.getenv('Y_COORDINATES'))
    group_id = os.getenv('VK_GROUP_ID')
    access_token = os.getenv('VK_GROUP_ACCESS_TOKEN')
    api_version = os.getenv('VK_API_VERSION')
    log_dir = os.path.join(BASE_DIR, os.getenv('LOG_DIR'))

    logging.basicConfig(
        level=logging.INFO,
        filename=log_dir,
        format='[%(asctime)s] %(levelname).1s %(message)s',
        datefmt='%Y.%m.%d %H:%M:%S')

    try:
        countdown = get_countdown(date_event)
        create_cover(
            countdown, cover_orginal_path, cover_final_path,
            font_path, color_rgb, color_size, x_coords, y_coords)
        upload_url = get_upload_url(group_id, access_token, api_version)
        vk_hash, vk_photo = upload_file(cover_final_path, upload_url)
        save_cover(vk_hash, vk_photo, access_token, api_version)
    except (Exception, KeyboardInterrupt) as e:
        msg = 'Got exception on main()'
        logging.exception(msg)
        sys.exit(msg)