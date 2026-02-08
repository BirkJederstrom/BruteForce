import hashlib

h = 'a688972e74f0d9227476bb32d20f95039082213f5030933f1905563a765ae004'

file_path = '1.txt'
x = 0
EasterEgg = True

try:
    with open(file_path, 'r') as file:
        print(file)
        for line in file:

            D = line.strip()

            if hashlib.sha256(D.encode()).hexdigest() == h:
                print("found pass: ", D)
                EasterEgg = False
                break

except:
    print("No file found.")

if EasterEgg:
    print("Go phishing!")


