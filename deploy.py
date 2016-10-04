#!/usr/bin/python

#import cgi
import json
import cgitb
import sys
cgitb.enable()

print "Content-Type: text/plain"
print

input = sys.stdin.read()
parsed_input = json.loads(input)

f = open('/usr/share/nginx/www/log.html','w')

secret = parsed_input['hook']['config']['secret']
f.write(secret)
