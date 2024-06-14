# Calculadora simples -- Julia e Samuel

while True:

    print('\n\t\t\t -- Calculadora -- ')

    print('1. soma')
    print('2. subtração')
    print('3. multiplicação')
    print('4. divisão')
    print('5. resto da divisão')
    print('6. sair')
    

    op = int(input('\n\tOpção: '))

    if op == 1:
        print('\n\t\t\t -- Soma --\n')
        
        num1 = int(input('\n\tNum1: '))
        num2 = int(input('\n\tNum2: '))
        
        resultado = num1 + num2 
        
        print('\n\tResultado: {}'.format(resultado))
    elif op == 2:
        print('\n\t\t\t -- Subtração --\n')
        
        num1 = int(input('\n\tNum1: '))
        num2 = int(input('\n\tNum2: '))
        
        resultado = num1 - num2
        
        print('\n\tResultado: {}' .format(resultado))
    elif op == 3:
        print('\n\t\t\t -- Multiplicação --\n')
        
        num1 = int(input('\n\tNum1: '))
        num2 = int(input('\n\tNum2: '))
        
        resultado = num1 * num2
        
        print('\n\tResultado: {}' .format(resultado))
    elif op == 4:
        print('\n\t\t\t -- Divisão --\n')
        
        num1 = int(input('\n\tNum1: '))
        num2 = int(input('\n\tNum2: '))
        
        resultado = num1 / num2
        
        print('\n\tResultado: {}' .format(resultado))
    elif op == 5:
        print('\n\t\t\t -- Resto da Divisão --\n')
        
        num1 = int(input('\n\tNum1: '))
        num2 = int(input('\n\tNum2: '))
        
        resultado = num1 % num2
        
        print('\n\tResultado: {}' .format(resultado))
    elif op == 6:
        print('\n Forte abraço!\n')
        break
    else:
        print('Opção {} incorreta!'.format(op))