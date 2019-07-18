x = 50
def func(x):
	global x
	print('x equals', x)
	x = 2
	print('Replace local x on', x)

func(x)
print('x still', x)
