#!python3

# pw.py - An insecure password locker program.
# run this program with a command line argument that is the account’s name—for instance, email or blog. 
#That account’s password will be copied to the clipboard so that the user can paste it into 
#a Password field. 

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
'luggage': '12345'}

import sys
if len(sys.argv) < 2:
	print('Usage: python pw.py [account] - copy account password')
	sys.exit()
account = sys.argv[1] # first command line arg is the account name
if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for ' + account + ' copied to clipboard.')
else:
	print('There is no account named ' + account)