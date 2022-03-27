import database.database_opening
from random import randrange, uniform

credenciaisBanco = database.database_opening.credencias()

def select_all():
    #db = credenciaisBanco
    cursor = database.database_opening.operator_db()

    cursor.execute("select * from job")
    resposta = cursor.fetchall()

    lista = []

    for i in resposta:
        objeto = i
        lista.append(i)

    cursor.close()
    return lista


def create_location():
    #opDB = credenciaisBanco
    cursor = database.database_opening.operator_db()

    street_address = input('Digite o endereco: ')
    city = input('Digite a Cidade: ')
    postal_code = input('Digite o Code Postal: ')
    state_province = input('Digite o Estado: ')

    cursor.execute("insert into location (street_address,postal_code,city,state_province) values('" + street_address + "','" + postal_code + "', '" +
            city + "', '" + state_province + "') ")

    #database.database_opening.operator_db().commit()

    print('*************Inserido com Sucesso************')

def update_local():
    #opDB = credenciaisBanco
    cursor = database.database_opening.operator_db()

    termo_busca = input("Digite o Local para operar: ")

    id = ""
    cursor.execute("select l.id from location l where l.street_address = '" + termo_busca + "' ")
    retorno = cursor.fetchone()

    for i in retorno:
        objeto = i
        id = objeto

    opcao = ""
    sql_update = ""

    print('Atualizar:\n1 - Endereco\n2 - Estado\n3 - Postal Code\n4 - Cidade')
    opcao = input('Digite a Opcao: ')

    if opcao == '1':
        novo_endereco = input('Digite o novo Endereco: ')
        sql_update = "update location set street_address = '"+novo_endereco+"' where id = "+str(id)+""
    elif opcao == '2':
        novo_estado = input('Digite o novo Estado: ')
        sql_update = "update location set state_province = '" + novo_estado + "' where id = " + str(id) + ""
    elif opcao == '3':
        novo_postalcode = input('Digite o novo Code Postal: ')
        sql_update = "update location set postal_code = '" + novo_postalcode + "' where id = " + str(id) + ""
    elif opcao == '4':
        nova_cidade = input('Digite a nova Cidade: ')
        sql_update = "update location set city = '" + nova_cidade + "' where id = " + str(id) + ""


    cursor_update = database.database_opening.operator_db()
    cursor_update.execute(sql_update)
    #database.database_opening.operator_db().commit()

    print('*************Atualizado com Sucesso********************')
