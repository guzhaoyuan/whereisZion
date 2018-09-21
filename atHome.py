# check if Zion is at home
# this is script is run by openWRT

from domain import homeDomain
import os

response = os.system("ping -q -c 1 %s > /dev/null" % homeDomain)  # output is system dependent

if response == 0:
    # notify server
    print("up!")
else:
    # notify server
    print("down!")

