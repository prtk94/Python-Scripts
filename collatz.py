
def collatz(num):
	if num%2 == 0:
		num = num/2
	elif num%2 == 1:
		num= 3*num + 1
	return num

try:
	num = int(input("Enter a num"))	
	while num != 1:	
		num= collatz(num)
		print(num)	
	
	print("You reached the end of collatz structure")
except Exception as e:
	print("Entr a number you dumbass")
	print(e)


