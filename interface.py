def readInteger(msg):
    while True:
        try:
            value = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;31mERROR! Invalid value.\033[m')
        except(KeyboardInterrupt):
            print()
            header('System closed... Come back later!')
            value = 0
            return value
        else:
            return value


def lign(len=42):
    return '-' * len


def header(txt):
    print(lign())
    print(txt.center(42))
    print(lign())


def menu(list):
    header('MENU')
    count = 1
    for item in list:
        print(f'\033[33m{count} -\033[m \033[34m{item}\033[m')
        count = count + 1
    print(lign())
    option = readInteger('\033[32mSua opção: \033[m')
    return option

