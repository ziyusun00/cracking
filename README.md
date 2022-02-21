# Cracking Password
## Introduction:
This project uses python to create a program that decrypt encrypted hexadecimal characters in order to determine the corresponding plain text password.
Given a list of password digests (hashes.txt), this program should be able to cracking passwords one by one, and generate a output file (cracked.txt) with format < hash >:< password >. 
All of the hashes in input file were hashed using SHA256. All passwords are salted with the randomly generated salt (salt.txt). 

## Decryption Method:
### 1. Dictionary attack
Using rockyou.txt which is a common passwords file pull from internet.
Using 20k.txt which is a common english words (no capitalization) file pull from internet.
Using 11to26.txt which is a long english words (11-26 characters) file pull from internet.

### 2. Brute force attack
Try all random strings (up to 4 characters in lowercase letters, numbers) using python's itertools module which provides various functions that work on iterators to produce complex iterators.

## Conclusion：
A total of 46 of the 55 codes were successfully cracked.
