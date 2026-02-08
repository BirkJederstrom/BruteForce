import hashlib

h = 'f5ce9571a545aa61d8bfc50050fa8e56'

# Test cases for the DB
'''
test = 'W@Q!W@Q!W@Q!r4e3'

h = hashlib.md5(test.encode()).hexdigest()
i = 0
print(test)
print(h)
'''
#replace file_path with correct path and/or file
file_path = '2.txt'
x = 0
EasterEgg = True

try:
    with open(file_path, 'r') as file:
        for line in file:
            #D = '{:04d}'.format(x)
            #print(line.strip())

            D = line.strip()
            
            if hashlib.md5(D.encode()).hexdigest() == h:
                print("found pass: ", D)
                EasterEgg = False
                break
except:
    print("No file found.")

if EasterEgg:
    print("Go phising!")

