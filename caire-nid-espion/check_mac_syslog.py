import re

# Open the syslog file syslog
with open("syslog.txt", "r") as f:
    syslog = f.read().splitlines()

# Check if there is a mac address in macs_clean that is in macs.txt
with open("macs.txt", "r") as f:
    macs_list = f.read().splitlines()

for line in syslog:
    for mac in macs_list:
        if mac in line:
            print(line)
            print(mac)
            print("")