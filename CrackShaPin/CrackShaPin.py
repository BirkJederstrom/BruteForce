import hashlib

h = "93a82987d3cdd931cd785dc93fddd305de9b488a"
x = 0

'''
encryption = ''
print("Write encryption!")

InputValidation = True

while(InputValidation):
    try:
        EncryptionInput = input("Encryption: ")

        EncryptionInput.lower()

        match EncryptionInput:
            case "sha1":
                encryption = 'sha1()'
            case "sha224":
                encryption = 'sha224()'

            #sha1(), sha224(), sha256(), sha384(), sha512(), sha3_224(), sha3_256(), sha3_384(), sha3_512(), shake_128(), shake_256(), blake2b(), and blake2s(). 

    except:
        print("Not a valid encryption!")

        
print("Your encryption is ", InputValidation)

salt = input("Enter salt: ")

try:
    print("Write salt if applicable. If left empty, does nothing.")
    salt = input("Enter salt: ")

    for x in range(9999):
        D = '{:04d}'.format(x)

        if hashlib.sha1(D.encode)

except:

    '''

for x in range(9999):
    D = '{:04d}'.format(x)

    if hashlib.sha1(D.encode()).hexdigest() == h:
        print("Found pass ", D)
        break
