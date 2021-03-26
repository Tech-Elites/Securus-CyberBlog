import time
from selenium import webdriver
from datetime import datetime as dt
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
import re

cred_object = firebase_admin.credentials.Certificate('#private key for connection to the database')
default_app = firebase_admin.initialize_app(cred_object, {
    'databaseURL': 'https://securus-bf653-default-rtdb.firebaseio.com/'
})
ref = db.reference('UserPosts')
details = ref.get()
links = []
for key, value in details.items():
    for k,v in value.items():
            if(k!='count'):
                if(v['link'] not in links):
                    links.append(v['link'])
                    if(re.search("^[a-zA-Z][a-zA-Z]+\.com$",v['link'])):
                        links.append("www."+v['link'])
#print(links)

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://google.com")
# change hosts path according to your OS
hosts_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"
# localhost's IP
redirect = "127.0.0.1"


def clearHost():
    with open(hosts_path, 'w') as file:
        original_comments = """# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host

# localhost name resolution is handled within DNS itself.
#	127.0.0.1       localhost
#	::1             localhost
"""
        file.write(original_comments)


while True:

    # time of your work

    # print("Working hours...")
    with open(hosts_path, 'r+') as file:
        content = file.read()
        for website in links:
            if website in content:
                pass
            else:
                # mapping hostnames to your localhost IP address
                file.write(redirect + " " + website + "\n")
    try:
        if(len(driver.window_handles) == 0):
            continue
    except:
        clearHost()
        break