import parser


# test lambdify func

print('\n\n\n\n')
active = True

while active == True:
    print('----test func triggered----')
    print('type \'n\' to terminate')
    test_input = input('enter function to be lambdified: ')
    if test_input == 'n':
        active = False
    else:
        print(str(parser.parse_input(test_input)))