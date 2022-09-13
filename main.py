
from modules.interface import *
from modules.archive import *
from time import sleep
arquivo = 'Base de dados.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)


while True:
    escolha = menu(['Ver lista de pessoas registadas', 'Novo registo', 'Sair do sistema'])

    if escolha == 1:
        lerArquivo(arquivo)
    elif escolha == 2:
        print()
        print('NOVO REGISTO')
        print()

        while True:
            try:
                while True:
                    nome = str(input('Nome completo: '))
                    nomev = nome
                    nome = nome.replace(' ', '')
                    if nome.isalpha():
                        nomev = nomev.strip().split()
                        ' '.join(nomev)
                        pessoa = ' '.join([str(item.capitalize()) for item in nomev])
                        break

            except (ValueError, TypeError):
                print('\033[1;31mErro! Por favor, digite uma opção válida.\033[m')
            except KeyboardInterrupt:
                exit('\n<<< Sistema Encerrado >>>')
            else:
                idade = leiaInteiro('Idade: ')
                registar(arquivo, pessoa, idade)
                break

    elif escolha == 3:
        print('<<< Sistema Encerado >>>')
        break
    else:
        print('\033[1;31mErro! Por favor, digite uma opção válida.\033[m')
        sleep(1)

