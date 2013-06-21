#! /usr/bin/python

import urllib2
from datetime import datetime
from time import sleep

with open("long_term_wifi.txt", "a") as wifi_file:
    while True:
        try:
            urllib2.urlopen("http://www.google.com", timeout=1)
            print "pass"
            wifi_file.write("pass ")
        except urllib2.URLError:
            print "fail"
            wifi_file.write("fail ")

        sleep(60)
