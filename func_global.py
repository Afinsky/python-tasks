x = 50
def func():
	global x
	print('x equals', x)
	x = 2
	print('Replace local x on', x)

func()
print('x still', x)
