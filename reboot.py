#! /usr/bin/python

from subprocess import call
from time import sleep
import urllib2

#sleep to give me time to remove this when I need to
sleep(120)

with open("reboot_nums.txt", "a") as reboot_file:
    reboot_file.write("1 ")

with open("wifi_test.txt", "a") as wifi_file:
    try:
        response=urllib2.urlopen("http://74.125.113.99", timeout=1)
        wifi_file.write("pass ")
    except urllib2.URLError:
        wifi_file.write("fail ")

call(["reboot"])
