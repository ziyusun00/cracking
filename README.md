# Cracking Password
## Introduction:
This project uses python to create a program that decrypt encrypted hexadecimal characters in order to determine the corresponding plain text password.
Given a list of password digests (hashes.txt), this program should be able to cracking passwords one by one, 
and generate a output file (cracked.txt) with format < hash >:< password >. 
All of the hashes in input file were hashed using SHA256. All passwords are salted with the randomly generated salt (salt.txt). 

## Decryption Method:
The first step is open the salt.txt and read the salt which is used to salt the possible password. 
Opening the document hashes.txt to read decrypted characters in each line and save as all_password.

### 1. Dictionary attack
The core method of dictionary attack is to open txt files that pull from internet, use line.strip() to clear spaces at the end of each line of data, 
and read characters in each line in turn, store them into variable test_password.
These characters are possible password combinations. Salting them to get salted_test_password, 
and then encoding them to UTF-8 using sha256 function in hashlib which returns hexadecimal hashed_test_password. 
Compare the elements in hashed_test_password with the elements in all_password one by one. 
If they are the same, print them in format < hashed_test_password >:< test_password >,
and append the current element of hashed_test_password into pass_password.
Finally, screening rest_password by selecting elements in all_password that are not 
in pass_password to facilitate the continuation of other kinds of attack attempts.

First, reading rockyou.txt file which is a common passwords file pull from internet.
Secondly, reading 20k.txt file which is a common english words file pull from internet for first letter capitalization situation, 
all uppercase letters situation, and all lowercase letters situation. Only first letter capitalization situation can decrypt passwords, so only keep it. 
Finally, reading 11to26.txt file which is a long english words (11-26 characters) file pull from internet.

### 2. Brute force attack
Try all random strings (up to 4 characters in lowercase letters, numbers) using python's itertools module, 
which provides various functions that work on iterators to produce complex iterators, set the repeat time to 1 to 4 respectively.
Storing these random strings into char_password, salting them to get salted_char_brute_password,
and encoding them to UTF-8 using sha256 function in hashlib which returns hexadecimal hashed_char_brute_password.
Compare the elements in hashed_char_brute_password with the elements in char_password one by one.
If they are the same, print them in format < hashed_char_brute_password >:< char_password >, 
and append the current element of hashed_char_brute_password into a new list named pass_password_2.
Creating list named rest_password_2 to store passwords in rest_password but not in pass_password_2.

## Conclusion：
A total of 49 of the 55 codes were successfully cracked.
All decryption results are printed on the console as < hashed_test_password >:< test_password > during the program run. 
The unsuccessfully decrypted passwords are also printed on the console as < rest_password >:< space >.
Copy and paste all the console run results into an output file named cracked.txt that clearly shows the decrypted results