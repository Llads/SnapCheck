import requests, threading, time, ctypes, string, random, sys
from colorama import init, Fore

ctypes.windll.kernel32.SetConsoleTitleW("SnapCheck v1.0.0")

text = """
  ______                   _______ _                 _     
 / _____)                 (_______) |               | |    
( (____  ____  _____ ____  _      | |__  _____  ____| |  _ 
 \____ \|  _ \(____ |  _ \| |     |  _ \| ___ |/ ___) |_/ )
 _____) ) | | / ___ | |_| | |_____| | | | ____( (___|  _ ( 
(______/|_| |_\_____|  __/ \______)_| |_|_____)\____)_| \_)
                    |_|                                   

"""

print(Fore.YELLOW + text)
print(Fore.YELLOW + "============================================")

speed = 1
num = 0


f = open('ToCheck.txt', 'r')
namesString = f.read()
names = namesString.split('\n')
f.close()


def save(names):
    with open('Available.txt', 'a', encoding='utf8') as f:
        f.write(names + '\n')

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://accounts.snapchat.com/",
    "Cookie": "xsrf_token=PlEcin8s5H600toD4Swngg; sc-cookies-accepted=true; web_client_id=b1e4a3c7-4a38-4c1a-9996-2c4f24f7f956; oauth_client_id=c2Nhbg==",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
}

i = 0

def checker():
    try:
        global i
        url = "https://accounts.snapchat.com/accounts/get_username_suggestions?requested_username={}&xsrf_token=PlEcin8s5H600toD4Swngg".format(names[i])
        r = requests.post(url, headers=headers)
        data = r.json()

        status = data.get("reference").get("status_code")

        if status == "OK":
            print(Fore.GREEN + names[i] + " is available")
            save(names[i])
        elif status == "TAKEN":
            print(Fore.RED + names[i] + " is unavailable")
        i += 1
    except IndexError as e:
        sys.exit(0)

while True:
    if threading.active_count() < 150:
        threading.Thread(target=checker, args=()).start()
        time.sleep(speed)
        num += 1
