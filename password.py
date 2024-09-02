
passwordFile = open('SecretPasswordFile.txt')
secretPassword = passwordFile.read()

print('Enter your password')
typedPassword = input()

if typedPassword == secretPassword:
    print('Access Granted')
if typedPassword == '12345':
        print('That password is one that an idiot puts on their luggage')
elif typedPassword != secretPassword:
    print('Access denied')