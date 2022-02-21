import itertools, hashlib, math

# read salt.txt
with open("/Users/sunziyu/Desktop/salt.txt", "r") as f:
  salt = f.read().strip()

# dictionary attack
# store the cracked passwords into list all_password
pass_password = []
with open("/Users/sunziyu/Desktop/rockyou.txt", "r", errors='ignore') as f:
  for line in f:
    # strip new line character
    test_password = line.strip()
    # concat salt and password, encode to utf-8
    salted_test_password = (salt + test_password).encode('utf-8')
    # hash salted password
    hashed_test_password = hashlib.sha256(salted_test_password).hexdigest()
    with open("/Users/sunziyu/Desktop/hashes.txt", "r") as k:
      for line in k:
        real_password = line.strip()
        if real_password == hashed_test_password:
          pass_password.append(real_password)
          print(real_password + ":" + test_password)

# store all the passwords into list all_password
all_password = []
with open("/Users/sunziyu/Desktop/hashes.txt", "r") as k:
  for line in k:
    real_password = line.strip()
    all_password.append(real_password)

# two lists both have exist_password
exist_password = [x for x in all_password if x in pass_password]
# rest_password list is the rest of passwords that weren't cracked
rest_password = [y for y in (all_password + pass_password) if y not in exist_password]

# brute-force attack
chars = '01234567890abcdefghijklmnopqrstuvwxyz'
pass_password = []
for i in itertools.product(chars, repeat=4):
    pass_password.append(''.join(i))
for i in itertools.product(chars, repeat=3):
    pass_password.append(''.join(i))
for i in itertools.product(chars, repeat=2):
    pass_password.append(''.join(i))
for i in itertools.product(chars, repeat=1):
    pass_password.append(''.join(i))

#check if brute froce cracked any password
for x in pass_password:
    salted_test_brute_password = (salt + x).encode('utf-8')
    hashed_test_brute_password = hashlib.sha256(salted_test_brute_password).hexdigest()
    for y in rest_password:
        if hashed_test_brute_password == y:
            print(y + ":" + x)


