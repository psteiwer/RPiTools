import json
import subprocess
import smtplib

## sudo apt-get install python2
## sudo apt-get install ssmtp
## sudo nano /etc/ssmtp/ssmtp.conf

with open("OldIPs.json","r") as oldipsfile:
    oldips=json.load(oldipsfile)

    oldexternal=oldips["External"]
    oldinternal=oldips["Internal"]

    print oldexternal
    print oldinternal

    retval=subprocess.check_output(["ifconfig","wlan0"])

    newinternal=retval[retval.find("inet addr:")+10:retval.find(" Bcast:")-1]

    if oldinternal!=newinternal:
        print "internal changed"
        print oldinternal
        print newinternal
    else:
        print "internal the same"

    newexternal=subprocess.check_output(["curl","ifconfig.me"])

    if oldexternal!=newexternal:
        print "external changed"
        print oldexternal
        print newexternal
    else:
        print "external the same"
