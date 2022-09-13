def leiaInteiro(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO! Digite um valor válido.\033[m')
        except(KeyboardInterrupt):
            print()
            cabeçalho('Sistema Encerrado... Volte sempre!')
            valor = 0
            return valor
        else:
            return valor


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    count = 1
    for item in lista:
        print(f'\033[33m{count} -\033[m \033[34m{item}\033[m')
        count = count + 1
    print(linha())
    opção = leiaInteiro('\033[32mSua opção: \033[m')
    return opção

