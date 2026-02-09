# BruteForce

The purpose of this script is used for educational purposes
The only allowed usage is within the University course 'SÄK2' at Stockholms Universitet
The author takes no responsibility if this script causes harm to your own machine
Any use of this script with the intention to harm, breach, or other malicious activity is discourage
The author takes no responsibility if this script is used maliciously

# Instructions

Run in correct folder containing the zip "Lab_2.zip"

## Remember

find ~/ -name "instruction"
find . -name "filename"
find . -type f -name 'btree*.c'

for ((count=1; count<=9999; count++)); do
  password=$(printf "%04d" "$count")

  if unzip -P "$password" archive.zip >/dev/null 2>&1; then
    echo "Password found: $password"
    break
  fi
done




Authored by Birk Jederström
