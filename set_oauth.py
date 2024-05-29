import os
import requests
from datetime import datetime, timezone

def get_access_token(code):
    auth_data = {
        'grant_type': 'authorization_code',
        'client_id': os.getenv('UID'),
        'client_secret': os.getenv('SECRET'),
        'code': code,
        'redirect_uri': 'https://profile.intra.42.fr/'
    }

    response = requests.post('https://api.intra.42.fr/oauth/token', data=auth_data)

    if response.status_code == 200:
        response_data = response.json()
        return response_data['access_token'], response_data['expires_in']
    else:
        return None, None


def get_days_until_blackhole(blackhole_date_str):
    blackhole_date = datetime.fromisoformat(blackhole_date_str[:-1]) # 마지막 'Z' 제거
    blackhole_date = blackhole_date.replace(tzinfo=timezone.utc) # Aware 객체로 변환
    today = datetime.now(tz=timezone.utc) # 현재 시간을 UTC 시간대로 가져오기
    delta = blackhole_date - today # 블랙홀까지 남은 시간 계산
    return delta.days + 1

def get_user_info(access_token, intra_id):
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(f'https://api.intra.42.fr/v2/users/{intra_id}', headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception('Failed to get user info')
