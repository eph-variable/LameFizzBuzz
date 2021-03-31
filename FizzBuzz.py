count = 0
n = 1
while 0 < n:
	count = count + 1
	if count % 3 == 0 and count % 5 == 0:
		print("FizzBuzz")
	elif count % 3 == 0:
		print ("Fizz")
	elif count % 5 == 0:
		print ("Buzz")
	else:
		print(count)
	if count == 1000:
		break
	



