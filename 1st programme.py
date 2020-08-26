while True:
    print('who are you?')
    name = input()
    if name != 'Batman':
        continue
    print('hello there '+name+'. What is this passcode?')
    password = input()
    if password == 'icecreamtruck':
        break
print('Enter batcave')
