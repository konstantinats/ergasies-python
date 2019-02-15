openfile=open("arxeio.py", 'r')
x=openfile.readlines()
openfile.close()
for line in x:
	xoriskena=line.rstrip()
	megethos=len(xoriskena)
	done=False
	if xoriskena[0]!="#":
		for i in range(0,megethos):
			if (xoriskena[i]=="#"):
				done=True
				thesi=i
		if (done==False):
			print (xoriskena)
		else:
			done1=False
			done2=False
			for j in range(thesi,megethos):
				if(xoriskena[j]=='"' or xoriskena[j]=="'"):
					done1=True
			for k in range(0,thesi):
				if (xoriskena[k]=='"' or xoriskena[k]=="'"):
					done2=True
			if (done1==True and done2==True):
				print(xoriskena)
			else:
				print(xoriskena[:thesi-1])