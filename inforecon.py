#!/usr/bin/env python
# coding: utf-8
# This code is meant to gather geographical coordinates of a host. 
# IT ONLY WORKS ON HTTPS
'''
First project 03/2022
@Witch_Sec
https://github.com/miss-anthrope
'''

import sys 
import requests
import socket
import json

print("\n")
print("Welcome to the inforecon code. This was made along with the UDemy python for pentesters course in March, 2022.")
print("\nPlease note: This string only works on HTTPS.")

if len(sys.argv) < 2:
	print("Useage: " + sys.argv[0] + "<url>")
	sys.exit(1)

req = requests.get("https://"+sys.argv[1])
print("\n"+str(req.headers))

gethostby_=socket.gethostbyname(sys.argv[1])
print("\nThe IP of "+sys.argv[1]+" is: "+gethostby_ + "\n")

#ipinfo.io is the API here

req_two = requests.get("https://ipinfo.io/"+gethostby_+"/")
resp_ = json.loads(req_two.text)

print("Location: "+resp_["loc"])
print("Region: "+resp_["region"])
print("City: "+resp_["city"])
print("Country: "+resp_["country"])
print("\nThank you. Goodbye!")
