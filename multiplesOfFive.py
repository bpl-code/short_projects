def totalSumOfMultiples(userNum):
    
	total = 0
	
	for i in range(userNum):
		if i%3 == 0:
			total += i
			print(str(i) + " was added")
		elif i%5 == 0:
			total += i
			print(str(i) + " was added")
	
	print("The Total sum of all multiples of 3 & 5 within " + str(userNum))
	print("equals " + str(total))
	return total
		
		
totalSumOfMultiples(1000)