x = input("input number: ")
fib1 = 1
fib2 = 1
i = 0
sum = 0
fib_sum = 0
while (fib1 + fib2) < int(x) :	
	 fib_sum = fib1 + fib2
	 if (fib_sum % 2) == 0 :
	 	sum += fib_sum
	 fib1 = fib2
	 fib2 = fib_sum

#	 print(fib_sum)
print()
print("Sum is: " + str(sum))
