import copy

def bsort(mylist):
	final_list=[]

	for i in range(0,len(mylist) -1):
		for j in range(0,len(mylist) -1 -i):
			if (int(mylist[j]) > int(mylist[j+1])):
				temp=mylist[j] 
				mylist[j]=mylist[j+1]
				mylist[j+1]=temp
				print(mylist)
		final_list.append(copy.deepcopy(mylist))				


	return final_list		
	
		
#list1= [89,90,22,2,3,1] #pass them as numbers not in '1','2' etc
#list1 = input("Enter your input:").split(',')
#print(list1)

