import itertools, hashlib, math, re

# read salt.txt
with open("/Users/sunziyu/Desktop/salt.txt", "r") as f:
  salt = f.read().strip()

# store all the passwords into list all_password
all_password = []
with open("/Users/sunziyu/Desktop/hashes.txt", "r") as k:
  for line in k:
    real_password = line.strip()
    all_password.append(real_password)

# dictionary attack
pass_password = []
with open("/Users/sunziyu/Desktop/rockyou.txt", "r", errors='ignore') as f:
  for line in f:
    # strip new line character
    test_password = line.strip()
    # concat salt and password, encode to utf-8
    salted_test_password = (salt + test_password).encode('utf-8')
    # hash salted password
    hashed_test_password = hashlib.sha256(salted_test_password).hexdigest()
    for i in all_password:
      if i == hashed_test_password:
        if i not in pass_password:
          pass_password.append(i)
          print(i + ":" + test_password)
# rest_password list is the rest of passwords that weren't cracked
rest_password = [y for y in all_password if y not in pass_password]

# brute-force attack
chars = '01234567890abcdefghijklmnopqrstuvwxyz'
char_password = []
for i in itertools.product(chars, repeat=4):
    char_password.append(''.join(i))
for i in itertools.product(chars, repeat=3):
    char_password.append(''.join(i))
for i in itertools.product(chars, repeat=2):
    char_password.append(''.join(i))
for i in itertools.product(chars, repeat=1):
    char_password.append(''.join(i))

pass_password_2 = []
for x in char_password:
    salted_char_brute_password = (salt + x).encode('utf-8')
    hashed_char_brute_password = hashlib.sha256(salted_char_brute_password).hexdigest()
    for y in rest_password:
        if hashed_char_brute_password == y:
          print(y + ":" + x)
          pass_password_2.append(y)
# rest_password_2 list is the rest of passwords that weren't cracked
rest_password_2 = [y for y in rest_password if y not in pass_password_2]

# dictionary attack
pass_password_3 = []
with open("/Users/sunziyu/Desktop/20k.txt", "r", errors='ignore') as f:
  for line in f:
    # strip new line character
    file_password = line.strip()
    file_password = file_password.capitalize()
    # concat salt and password, encode to utf-8
    salted_file_password = (salt + file_password).encode('utf-8')
    # hash salted password
    hashed_file_password = hashlib.sha256(salted_file_password).hexdigest()
    for y in rest_password_2:
        if y == hashed_file_password:
          pass_password_3.append(hashed_file_password)
          print(y + ":" + file_password)
# rest_password_3 list is the rest of passwords that weren't cracked
rest_password_3 = [y for y in rest_password_2 if y not in pass_password_3]

# dictionary attack
pass_password_4 = []
with open("/Users/sunziyu/Desktop/11to26.txt", "r", errors='ignore') as s:
  for line in s:
    # strip new line character
    long_password = line.strip()
    salted_long_password = (salt + long_password).encode('utf-8')
    hashed_long_password = hashlib.sha256(salted_long_password).hexdigest()
    for y in rest_password_3:
        if y == hashed_long_password:
          pass_password_4.append(hashed_long_password)
          print(y + ":" + long_password)
# rest_password_4 list is the rest of passwords that weren't cracked
rest_password_4 = [y for y in rest_password_3 if y not in pass_password_4]

for i in rest_password_4:
  print(i + ":")

'''''
pass_password_5 = []
symbols = '!@#$%^&*-+=<>?'
with open("/Users/sunziyu/Desktop/20k.txt", "r", errors='ignore') as f:
  for line in f:
    # strip new line character
    name_password = line.strip()
    for i in itertools.product(symbols, repeat=1):
      name_password+''.join(i)
      salted_name_password = (salt + name_password).encode('utf-8')
      hashed_name_password = hashlib.sha256(salted_name_password).hexdigest()
      for y in rest_password_4:
          if y == hashed_name_password:
            pass_password_5.append(hashed_name_password)
            print(y + ":" + name_password)

two_words_password = []
for i in itertools.product(common_words, repeat=2):
    two_words_password.append(''.join(i))
for x in two_words_password:
    salted_two_words_password = (salt + x).encode('utf-8')
    hashed_two_words_password = hashlib.sha256(salted_two_words_password).hexdigest()
    for y in rest_password_4:
        if hashed_two_words_password == y:
          print(y + ":" + x)
'''''