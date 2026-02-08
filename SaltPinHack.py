import hashlib

nonSaltHash = "93a82987d3cdd931cd785dc93fddd305de9b488a"
x = 0

salt = '1fa6'

h = nonSaltHash + salt

print(h)

for x in range(9999999):
    D = '{:04d}'.format(x)
    print(D)

    if hashlib.sha3_512(D.encode()).hexdigest() == h:
        print("Found pass ", D)
        break

