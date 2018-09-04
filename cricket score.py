#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 22:35:14 2018

@author: vishal
"""


import requests
from bs4 import BeautifulSoup
from gi.repository import Notify
from time import sleep
def displaymessage(title, message):
    Notify.init("Test")
    notice = Notify.Notification.new(message)
    notice.show()
    return
url = "http://static.cricinfo.com/rss/livescores.xml"
while True:
    r = requests.get(url)
    #now we use r.status_code to check whether all is well or not
    #r.status_code having the value 200 means that all is well otherwise connection have some problem.
    while r.status_code is not 200:
            r = requests.get(url)
    soup = BeautifulSoup(r.text)
    data = soup.find_all("description")
    score = data[6].text
    displaymessage("Score", score)
    sleep(600)
