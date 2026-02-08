import hashlib

#Below follows the quick construction of the salted pin hash, used during testing

#pin = '7890'
#salt1 = '1fa6'
#h = hashlib.sha256((pin + salt1).encode()).hexdigest()

h = "93a82987d3cdd931cd785dc93fddd305de9b488a"
salt = '1fa6'
x = 0

for x in range(9999):
    D = ('{:04d}'.format(x) + salt)
    #print(D)

    if hashlib.sha256(D.encode()).hexdigest() == h:
        print("Found pass + salt: ", D)
        password = D.replace(salt, "")
        print("The Password: ", password)
        print("The salt was: ", salt)
        break
