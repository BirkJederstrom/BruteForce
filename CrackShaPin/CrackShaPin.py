import hashlib

h = "93a82987d3cdd931cd785dc93fddd305de9b488a"

D = [
    line[:4]
    for line in open("x")
    if len(line.strip()) >= 4 and line[:4].isdigit()
    ]

for p in D:
    if hashlib.sha1(p.encode()).hexdigest() == h:
        print("Found password: ", p)
        break

    print("No password found.")

