import hashlib

h = 'a688972e74f0d9227476bb32d20f95039082213f5030933f1905563a765ae004'
salt = ''

file_path = 'path/to/file.txt'
EasterEgg = True

try:
    with open(file_path, 'r') as file:
        print(file)
        for line in file:

            D = (line.strip() + salt)

            if hashlib.sha256(D.encode()).hexdigest() == h:
                print("found pass + salt: ", D)
                password = D.replace(salt, "")
                print("The Password: ", password)
                print("The salt was: ", salt)
                EasterEgg = False
                break

except:
    print("No file found.")

if EasterEgg:
    print("Go phishing!")

