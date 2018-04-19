import requests


def get_upload_url(group_id, access_token, api_version):
    url = 'https://api.vk.com/method/photos.getOwnerCoverPhotoUploadServer'
    params = {
        'group_id': group_id, 'crop_x': 0, 'crop_y': 0, 'crop_x2': 1590,
        'crop_y2': 400, 'access_token': access_token, 'v': api_version}
    r = requests.get(url, params=params)
    return r.json()['response']['upload_url']


def upload_file(file_path, upload_url):
    file = {'file': open(file_path, 'rb')}
    r = requests.post(upload_url, files=file)
    json_data = r.json()
    return json_data['hash'], json_data['photo']


def save_cover(vk_hash, vk_photo, access_token, api_version):
    url = 'https://api.vk.com/method/photos.saveOwnerCoverPhoto'
    params = {
        'hash': vk_hash, 'photo': vk_photo, 
        'access_token': access_token, 'v': api_version}
    return requests.get(url, params=params)