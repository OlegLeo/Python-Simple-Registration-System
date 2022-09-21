

def archiveExists(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def createArchieve(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print('Error Acquired on Creating Archieve File!')
    else:
        print(f'\033[32mArchieve, {name} created successfully!\033[0m')

def readArchive(name):
    try:
        a = open(name, 'rt')
    except:
        print('Error Acquired on Trying to Read the File!')
    else:
        print('Registrations')
        for l in a:
            data = l.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<30}{data[1]:>3} anos')
    finally:
        a.close()

def register(archive, name='unknown',age=0):
    try:
        a = open(archive, 'at')
    except:
        print('Error Acquired on Creating Archieve File!')
    else:
        try:
            a.write(f'{name};{age}\n')
        except:
            print('Error on reading file!')
