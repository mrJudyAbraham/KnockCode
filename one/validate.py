

def evaluate(a,b):
	stored_code = list(map(int,str(a)))
	input_code = list(map(int,str(b)))
	m=len(stored_code)
	n=len(input_code)
	f=True
	k=0
	if(m==n):
		for i in stored_code :
			
			if(i==input_code[k]):
				f=False
				print(i,"\t",input_code[k])
				k+=1	
			else:
				f=True
				break
		if(f==True):
			return 0
		else:
			return 1	
	else:
		return 0		


