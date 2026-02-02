#The purpose of this script is used for educational purposes
#The only allowed usage is within the University course 'SAK2' at Stockholms Universitet
#The author takes no responsibility if this script causes harm to your own machine
#Any use of this script with the intention to harm, breach, or other malicious activity is discourage
#The author takes no responsibility if this script is used maliciously
#Authored by Birk Jederstrom

import os
import subprocess

x = 0

#Non

def bruteforce():
    
    y = str(x)
    z = y.zfill(4)
    
    subprocess.run(["unzip", "-P", "'", z, "'", "Lab_2.zip"])

    #print("unzip -P '" + z + "' archive.zip")

x = 0
while x < 9999:
    x += 1
    bruteforce()
