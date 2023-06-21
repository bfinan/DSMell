## Daily script for automated tasks

import os, datetime, subprocess, random, requests
#from myosotis import *


AFTER_HOURS = False
if datetime.datetime.today().hour > 20:
    AFTER_HOURS = True
    print("After hours")

# print a header and today's date, formatted as "Today is Tuesday, July 1st"
def dateinfo():
    if not AFTER_HOURS:
        print("Today is " + datetime.datetime.today().strftime("%A, %B %d"))
    else:
        print(
            "Tomorrow is "
            + (datetime.datetime.today() + datetime.timedelta(days=1)).strftime("%A, %B %d")
        )

def autojanny():
    # run autojanny and push to git
    os_type = os.name
    if os.name == "nt":
        subprocess.run("cmd /c autojanny.sh", shell=True)
        subprocess.run("cmd /c push.sh", shell=True)
    else:
        subprocess.run("bash autojanny.sh 2 > /dev/null", shell=True)
        subprocess.run("bash push.sh 2 > /dev/null", shell=True)

## main function
def main():
    autojanny()

    # print "done" and the coffee emoji
    print("done ☕️")


if __name__ == "__main__":
    main()
