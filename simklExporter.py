import requests
from pandas import DataFrame
import configparser
import webbrowser
import pyautogui
import time
import json


client_id = ""  # insert simkl client_id in quotation marks here


def make_request(url, headers=None):
    response = requests.get(url, headers=headers)
    return response.json()


config = configparser.ConfigParser()

config.read('conf.ini')

get_pin_url = "https://api.simkl.com/oauth/pin?client_id=" + client_id

pin_request = make_request(get_pin_url)

user_code = pin_request['user_code']
verification_url = pin_request['verification_url']

is_user_authenticated = False
code_verification_url = "https://api.simkl.com/oauth/pin/" + user_code + "?client_id=" + client_id

# Automatic authentication:
try:
    print(
        "Automatic authentication is about to start.\nA browser window should pop up and the authentification code should be entered.\nPlease click 'Yes' afterwards and return to this.")
    input("Press enter to start")
    webbrowser.open_new_tab(str(verification_url))
    time.sleep(5)  # waiting for page to load
    pyautogui.typewrite(user_code)
    time.sleep(1)
    pyautogui.press('enter')
    print("Please wait...")
    time.sleep(5)
    print("Continuing")
    code_verification_request = make_request(code_verification_url)
    if 'access_token' in code_verification_request:
        access_token = code_verification_request['access_token']
        is_user_authenticated = True
except Exception as e:
    print("Error during automatic authentication:")
    print(e)
    is_user_authenticated = False

while not is_user_authenticated:
    print("Please go to " + verification_url + " and enter this Pin:")
    print(user_code)
    input("After confirming the code press enter...")
if not is_user_authenticated:
    code_verification_request = make_request(code_verification_url)
    if 'access_token' in code_verification_request:
        access_token = code_verification_request['access_token']
        is_user_authenticated = True

get_movies_list_url = "https://api.simkl.com/sync/all-items"

response = make_request(get_movies_list_url, {'Authorization': 'Bearer ' + access_token, 'simkl-api-key': client_id})

with open('./simklData.json', 'w') as f:
    json.dump(response, f)

for category, value in response.items():
    df = DataFrame.from_dict(response[category])
    df.to_csv(f"./simklData_{category}.csv", encoding='utf-8', index=False)

print("Backup finished")
