from set_oauth import get_access_token, get_days_until_blackhole, get_user_info
import os
from dotenv import load_dotenv
from ascii_art import add_border

load_dotenv()

target_uri = os.getenv("TARGET_URI")
if target_uri == None:
    print('Failed to get TARET_URI from .env file')
    exit(0)

print(add_border(' Go to the following link and get the code '))
print(target_uri + '\n')

while True:
    code = input('>> Enter the code here (or type "exit" to quit): ')
    if code == 'exit':
        exit(0)
    access_token, expires_in = get_access_token(code)
    if (access_token == None):
        print('Failed to get access token')
        continue
    break

print(add_border('access_token = ' + access_token))

while True:
    intra_id = input('>> Enter intra ID here (or type "exit" to quit): ')
    if intra_id == 'exit':
        exit(0)

    try:
        user_info = get_user_info(access_token, intra_id)
        is_blackholed = False
        for cursus_user in user_info['cursus_users']:
            if cursus_user['blackholed_at']:
                days_until_blackhole = get_days_until_blackhole(cursus_user['blackholed_at'])
                is_blackholed = True
                break
        if is_blackholed:
            print(add_border(f"{intra_id}'s blackhole in {days_until_blackhole} days"))
        else:
            print(add_border(f"{intra_id} is not blackholed, maybe {intra_id} is member"))

    except:
        print(add_border(intra_id, "is not found"))
        continue