x = 1000

i = 0
sum = 0

while i < x :
	if (i % 3) == 0 or (i % 5) == 0 :
		sum += i
	i = i + 1

print(sum) 