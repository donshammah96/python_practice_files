
while True:
    print('Please type your name.')
    name = input()
    if name != 'Don':
        continue
    print('Hello Don, what is your password? Hint: it is a fish')

    password = input()
    if password == 'swordfish':
     print('Access Granted!')
     break
    