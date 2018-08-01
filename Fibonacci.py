def Fib(n) :
	a,b,temp,res=0,1,0,0
	
	if n==1 :
		res=a
	elif n==2 :
		res=b
	else :
		for x in range(0,n-2):
			temp=a+b
			a=b
			b=temp
			res=temp		 
		 
	print(res)	 

	user_input= int(input("Enter a number:"))
Fib(user_input)
	