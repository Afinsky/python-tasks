shoplist = ['apples', 'mango', 'carrot', 'bananas']
print('I must do', len(shoplist), 'buying')
print('buying:', end=' ')
for item in shoplist:
	print(item, end=' ')

print('\nAlso need buy rice')
shoplist.append('rice')
print('Now my shoplist:', shoplist)

print('I sort my shoplist')
shoplist.sort()
print('Sorted shoplist look like:', shoplist)

print('First me need buy ', shoplist[0])

olditem = shoplist[0]
del shoplist[0]

print('I bought', olditem)
print('Now my shoplist:', shoplist)