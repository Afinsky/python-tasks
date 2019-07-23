import sys, os


def func(initial=5, *, extra_number):
	count = initial
	for number in range(1,10):
		count += number
	count += extra_number
	print(count)

func(extra_number=10)



print(sys.path, '\n')
print(os.getcwd())