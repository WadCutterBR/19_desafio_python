menu = '''

    **MENU**

    (1) Depositar
    (2) Sacar
    (3) Extrato
    (4) Sair

    ********
'''
saldo, limite, extrato, saques, limite_saque = 0,500,"",0,3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do deposito: \n"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito no valor de R$ {valor:.2f}\n"
            print(f"R$ {valor:.2f} depositado com sucesso!")

        else:
            print("Falha na Operação, Digite um valor VÁLIDO")
    
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: \n"))

        if valor > saldo:
            print(" NEGADO, NÃO TEM SALDO DISPONÍVEL PARA SAQUE")

        elif valor > limite:
            print(" NEGADO, SAQUE ACIMA DO VALOR PERMITIDO")
        
        elif saques >= limite_saque:
            print(" NEGADO, EXCEDEU LIMITE DE SAQUES DA CONTA")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque no valor de R$ {valor:.2f}\n"
            saques += 1
            print(f"R$ {valor:.2f} sacado com sucesso!")

        else:
            print("Falha na Operação, Digite um valor VÁLIDO")
    
    elif opcao == '3':
        menu_extrato = f'''
        ** EXTRATO **

        {extrato}

        ** FIM DO EXTRATO **
        '''

        print(menu_extrato)

    elif opcao == '4':
        print("Obrigado por utilizar nossos serviços")

        break

    else:
       print("Operação inválida, por favor selecione novamente a operação desejada.\n") 

            
