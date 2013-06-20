#! /usr/bin/python

from subprocess import call
from time import sleep

with open("reboot_nums.txt", "a") as reboot_file:
    reboot_file.write("1 ")

#sleep to give me time to remove this when I need to
sleep(120)
call(["reboot"])
