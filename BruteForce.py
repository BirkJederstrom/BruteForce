#The purpose of this script is used for educational purposes
#The only allowed usage is within the University course 'SAK2' at Stockholms Universitet
#The author takes no responsibility if this script causes harm to your own machine
#Any use of this script with the intention to harm, breach, or other malicious activity is discourage
#The author takes no responsibility if this script is used maliciously
#Authored by Birk Jederstrom

import os
import subprocess

x = 0
PassFound = True
#Non

for x in range(9999):
    y = str(x)
    z = y.zfill(4)

    crack = subprocess.run(
        ["unzip", "-P", z, "-qq", "archive.zip"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    if crack.returncode == 0:
        print(f"Password found: {z}")
        break

