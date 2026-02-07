import hashlib

h = "93a82987d3cdd931cd785dc93fddd305de9b488a"
x = 0

for x in range(9999):
    D = '{:04d}'.format(x)

    if hashlib.sha1(D.encode()).hexdigest() == h:
        print("Found pass ", D)
        break