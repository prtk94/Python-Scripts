#!python3
'''
Password Strength Checker.
Input the password as a command line argument
Use regular expressions to make sure the password
string it is passed is strong. A strong password is defned as one that is at
least eight characters long, contains both uppercase and lowercase characters, 
and has at least one digit.
Also has a special character
'''
import re,sys

password= sys.argv[1]
count=0

if re.search(r"[A-Za-z]+",password):
	count+=1
if re.search(r"[0-9]+",password):
	count+=1
if len(password)>7 :
	count+=1
if re.search(r"[\*\+@#\$&]",password):
	count+=1

if count>3 :
	print("Password is strong")
else:
	print("Password is weak")
