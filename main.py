from set_oauth import get_access_token, get_days_until_blackhole, get_user_info
import os
from dotenv import load_dotenv

load_dotenv()

print('Go to the following link and get the code:\n', os.getenv("TARGET_URI"))
while True:
    code = input('Enter the code: ')
    access_token, expires_in = get_access_token(code)
    if (access_token == None):
        print('Failed to get access token')
        continue
    break

print('access_token = ', access_token, 'expires_in = ', expires_in)

while True:
    intra_id = input("Enter your intra ID: ")
    if intra_id == 'exit':
        break

    try:
        user_info = get_user_info(access_token, intra_id)
        is_blackholed = False
        for cursus_user in user_info['cursus_users']:
            if cursus_user['blackholed_at']:
                days_until_blackhole = get_days_until_blackhole(cursus_user['blackholed_at'])
                is_blackholed = True
                break
        if is_blackholed:
            print(f"{intra_id}'s blackhole in {days_until_blackhole} days")
        else:
            print(f"{intra_id} is not blackholed, maybe {intra_id} is member")

    except:
        print(intra_id, "is not found")
        continue