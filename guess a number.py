n=68
t=8
for i in range(0,6):
	num=int(input(" guess a number"))
	if i==5:
		print("0 attempt left!,you lost")
		break
	elif num>n:
		print("enter lower number please")
	elif num<n:
		print("enter higher number please")		
	elif num==n:
		print(" congo,you won!")
		break
if i<5:
	print("you guess it in",end=",")	
	print(i+1,end=" ")
	print("attempt")
else:
	pass
