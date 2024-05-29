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
        data = get_user_info(access_token, intra_id)

        # 42cursus에서 Learner인지 Member인지 구분
        for cursus_user in data['cursus_users']:
            if cursus_user['cursus_id'] == 21:  # 42cursus의 id는 21
                user_info = cursus_user

        grade = user_info['grade']
        if grade == 'Member':
            print(add_border(f" {intra_id} is Member "))
        else:
            days_until_blackhole = get_days_until_blackhole(user_info['blackholed_at'])
            print(add_border(f" {intra_id}'s blackhole in {days_until_blackhole} days" ))

    except:
        print(add_border(' ' + intra_id + " is not found " ))
        continue