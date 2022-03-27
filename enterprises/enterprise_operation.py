import database.database_opening
from random import randrange, uniform

credenciaisBanco = database.database_opening.credencias()

def select_all():
    cursor = database.database_opening.operator_db()

    cursor.execute("select * from enterprise")
    resposta = cursor.fetchall()

    lista = []

    for i in resposta:
        objeto = i
        lista.append(i)

    cursor.close()
    return lista

def create_enterprise():
    #opDB = credenciaisBanco
    cursor = database.database_opening.operator_db()

    foundation_name = input('Digite o nome da Empresa: ')
    email = input('Digite o E-mail: ')
    phone = input('Digite o Phone: ')

    identify = randrange(45 * 89) * 77

    cursor.execute("insert into enterprise (foundation_name,email,phone_number,id) values('" + foundation_name + "','" + email + "', '" +phone + "'," + str(identify) + " ) ")

    #database.database_opening.operator_db().commit()
    print('*************Inserido com Sucesso************')


def update_enterprise():
    cursor = database.database_opening.operator_db()

    termobusca = input('Digite o nome da Empresa: ')

    sql_update = ""

    cursor = database.database_opening.operator_db()
    id = ""
    cursor.execute("select e.id from enterprise e where e.foundation_name = '" + termobusca + "' ")

    retorno = cursor.fetchone()

    for i in retorno:
        objeto = i
        id = objeto


    opcao = ""


    print('Atualizar:\n1 - Foundation Name\n2 - Email\n3 - Phone')
    opcao = input('Opcao: ')

    if opcao == '1':
        novo_nome = input('Digite o novo nome: ')
        sql_update = "update enterprise set foundation_name = '"+novo_nome+"' where id = "+str(id)+""
    elif opcao == '2':
        novo_email = input('Digite o novo nome: ')
        sql_update = "update enterprise set email = '" + novo_email + "' where id = " + str(id) + ""
    elif opcao == '3':
        novo_phone = input('Digite o novo nome: ')
        sql_update = "update enterprise set phone_number = '" + novo_phone + "' where id = " + str(id) + ""

    cursor_update = database.database_opening.operator_db()
    cursor_update.execute(sql_update)
    #database.database_opening.operator_db().commit()
    print('Registro Atualizado com Sucesso!!!', termobusca)


def list_all():
    #db = credenciaisBanco
    cursor = database.database_opening.operator_db()

    cursor.execute("select foundation_name from enterprise")
    resposta = cursor.fetchall()

    lista = list()

    for i in resposta:
        objeto = str(i)
        lista.append(i)

    cursor.close()

    print(lista)