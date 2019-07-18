nummber = 23
running = True

while running:
    guess = int(input('input nummber : '))
    if guess == nummber:
        print('Congratulatinon!')
        running = False
    elif guess < nummber:
        print('No, u wrong. Conceived number is more') 
    else: 
        print('No, u wrong. Conceived number is less')
else:
    print('Cycle is end')   

print('end')