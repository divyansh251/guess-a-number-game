import random
n=random.randint(1,100)
print("you have 10 attempt to guess the number")
t=10
for i in range(0,10):
	num=int(input(" guess a number"))
	if i==9:
		print("0 attempt left!,you lost")
		break
	elif num>n:
		print("enter lower number please")
		t=t-1
		print(f"attempt left {t}!!!")
	elif num<n and n!=0:
		print("enter higher number please")
		t=t-1
		print(f"attempt left {t}!!!")			
	elif num==n:
		print(" congo,you won!")
		print("you guess it in",end=" ")
		print(i+1,end=" ")
		print("attempt")
		break
