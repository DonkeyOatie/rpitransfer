from subprocess import call
from time import sleep

with open("reboot_nums.txt", "a") as reboot_file:
    num = int(reboot_file.readline())
    num++
    reboot_file.write(num)

sleep(60)
call(["reboot"])
