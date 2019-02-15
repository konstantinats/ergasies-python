def sumIntervals(lista):
	sum = 0
	lista.sort()
	x = len(lista) - 1
	print(lista)
	for i in range(0, x):
		if (lista[i][1] > lista[i + 1][0]):
			if (lista[i][1] < lista[i + 1][1]):
				lista[i + 1][0] = lista[i][1]
			else:
				lista[i + 1][0] = 0
				lista[i + 1][1] = 0
	for i in range(0, len(lista)):
		sum += lista[i][1] - lista[i][0]
		
	print(sum)
	
	
	
lista[[1, 2],[7, 10],[3, 9],[415, 678],[1, 6],[199, 255]]
sumIntervals(lista)
