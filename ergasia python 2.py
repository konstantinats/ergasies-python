num = int(input("Enter a number: "))
if (num > 1):
	ar=num
	p=1
	j=1
	k=0
	for i in range(2,ar):
		if ((ar % i) == 0):
			print(num,"is not a prime number")
			break
		else:
			print(num,"is a prime number")
	while (p==num):
		j +=1
		while (ar%j == 0):
			ar=ar//j
			k +=1
			break
		p=p*i**k
	print ("(", i, "**", k, ")")
else:
   print(num,"is not a prime number")