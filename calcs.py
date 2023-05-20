while True:
    print('Olá, eu sou Vitória, a sua calculadora particular, irei lhe ajudar a resolveros cáculos')
    numero1 = input('digite um numero ')
    operador = input('Digite um operador ')
    numero2 = input('Digite outro número ')

    operadores_validos = '+-*/'

    numeros_validos = None

    try:
        numerofloat = float(numero1)
        numerofloat2 = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
       print('Por favor digite um número válido')
       continue

    if operador not in operadores_validos:
        print('Por favor, digite um operador de cálculo')
        continue

    if len(operador) > 1:
        print('Por favor, insira apenas "1" operador, para realizar a operação')
        continue

    soma = numerofloat + numerofloat2
    subtração = numerofloat - numerofloat2
    multiplicação = numerofloat * numerofloat2
    divisão = numerofloat / numerofloat2
    
    
    if operador == '+':
        print(soma)
    elif operador == '-':
        print(subtração)
    elif operador == '*':
        print(multiplicação)
    elif operador == '/':
        print(divisão)
    else:
        print('oppsss!! Não entendi seu cálculo...')

    sair = input('Você deseja sair? ').startswith('s')
    if sair is True:
        print('Obrigado, adorei sua companhia...volte sempre!')
        break