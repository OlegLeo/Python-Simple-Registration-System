from interface import *
from archive import *
from time import sleep
archive = 'Data_Base.txt'

if not archiveExists(archive):
    createArchieve(archive)


while True:
    choice = menu(['Show list of Registered people', 'New Registration', 'Quit Program'])

    if choice == 1:
        readArchive(archive)
    elif choice == 2:
        header('New Resgistration')
        while True:
            try:
                while True:
                    name = str(input('Full Name: '))
                    namev = name
                    name = name.replace(' ', '')
                    if name.isalpha():
                        namev = namev.strip().split()
                        ' '.join(namev)
                        person = ' '.join([str(item.capitalize()) for item in namev])
                        break

            except (ValueError, TypeError):
                print('\033[1;31mError! Please, whatch out the insertion of characters.\033[m')
            except KeyboardInterrupt:
                exit('\n<<< Program Finished >>>')
            else:
                age = readInteger('Age: ')
                register(archive, person, age)
                break

    elif choice == 3:
        print('<<< Program Finished >>>')
        break
    else:
        print('\033[1;31mErro! Please, insert the right value.\033[m')
        sleep(1)
