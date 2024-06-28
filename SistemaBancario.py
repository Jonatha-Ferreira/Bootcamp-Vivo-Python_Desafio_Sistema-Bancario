import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

saldo = 0
deposito = ""
saque = ""
quantidade_de_saques_realizados = 0

def realizar_deposito(valor_deposito):
    global saldo
    global deposito
    
    if valor_deposito > 0:
        saldo += valor_deposito
        
        deposito += f"Depósito: {locale.currency(valor_deposito, grouping=True)}\n"

    else: 
        return print("Operação falhou! Valor inválido!")

def realizar_saque(valor_saque):
    global saldo
    global saque
    global quantidade_de_saques_realizados

    VALOR_MAXIMO_POR_SAQUE = 500
    QUANTIDADE_DE_SAQUES_DIARIO = 3
    

    if valor_saque > saldo:
        print("Não é possível realizar a operação, valor excede o saldo em conta!")

    elif quantidade_de_saques_realizados >= QUANTIDADE_DE_SAQUES_DIARIO:
        print("Não é possível realizar a operação, limite de saque diário atingido!")

    elif valor_saque > VALOR_MAXIMO_POR_SAQUE:
        print("Não é possível realizar a operação, valor acima do limite!")

    elif valor_saque > 0:
        saldo -= valor_saque
        quantidade_de_saques_realizados += 1
        saque += f"Saque: {locale.currency(valor_saque, grouping=True)}\n"

    else:
        return print("Operação falhou! Valor inválido!") 

def gerar_extrato():
    extrato = ""
    extrato = saque + deposito
    return print(f"--------------Extrato--------------\n{extrato}\nSaldo da conta: {locale.currency(saldo, grouping=True)}")

def operacao():
    while True:
        
        opcao = input(""" 
[d] Depositar              
[s] Sacar
[e] Extrato
[f] fechar 
                
=> """)
        match opcao:
            case "d":
                realizar_deposito(float(input("Informe o valor do depósito: ")))

            case "s":
                realizar_saque(float(input("Informe o valor do saque: ")))

            case "e":
                gerar_extrato()

            case "f":
                break

            case _:
                print("Operacao invalida, tente novamente!")


print(operacao())