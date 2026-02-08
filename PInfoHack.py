import hashlib

h = '60f9f675974e936dd4b1032280a290da16ea110ed985d3cc3d5cd968fe5ab7ed'
salt = 'e098'

file_path = '2.txt'
EasterEgg = True

try:
    with open(file_path, 'r') as file:
        print(file)
        for line in file:

            D = (line.strip() + salt)

            if hashlib.sha3_256(D.encode()).hexdigest() == h:
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

