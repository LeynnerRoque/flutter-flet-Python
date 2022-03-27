from time import sleep


def compose_tela():
    for i in range(10):
        print('\t*'*i)

def escreveTela(texto: str):
    for letra in texto:
        print(letra, end='', flush=True)
        sleep(0.04)
    print()


def escreveTela2(texto: str):
    for letra in texto:
        print(letra, end='', flush=True)
        sleep(0.10)
    print()

def escreveLetras():

    return 'AMOR\tPAZ\tESPERANÇA\tSAÚDE\tSOLIDARIEDADE'


def escreveLetras2():

    return 'BONDADE\tCARIDADE\tLUZ\tHUMILDADE'


def escreveFinal():
    return '\t\tJ\tE\tS\tU\tS\t!'


escreveTela('***************')
for i in range(5):
 escreveTela(escreveLetras())
 escreveTela(escreveLetras2())


escreveTela2(escreveFinal())
