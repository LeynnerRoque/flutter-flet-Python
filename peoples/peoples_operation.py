import database.database_opening
from random import randrange, uniform


credenciaisBanco = database.database_opening.credencias()


def select_all():
    cursor = database.database_opening.operator_db()

    cursor.execute("select * from peoples")
    resposta = cursor.fetchall()

    lista = []

    for i in resposta:
        objeto = i
        lista.append(i)

    cursor.close()
    return lista

#create Peoples
def add_peoples():
    cursor = database.database_opening.operator_db()

    name = input("Nome: ")
    gender = input("Genero: ")
    age = input("Idade: ")
    email = input("E-mail: ")
    region_name = input("Regiao: ")
    phone = input("Telefone: ")
    jobId = input("Digite o codigo do job: ")
    location = input("Digite o codigo da Location: ")

    identify = randrange(45 * 89) * 77

    query = "insert into peoples (name,gender,age,region_name,email,phone,job_id,location_id) values('"+name + "', '"+gender + "', '"+str(age) + "', '"+region_name + "', '"+email + "', '"+phone + "', "+jobId+" , "+location+")"

    cursor.execute(query)

    #database.database_opening.operator_db().commit()
    print('*************Inserido com Sucesso************')


def update_peoples():
        db = credenciaisBanco
        termobusca = input("Digite o Nome: ")

        sql_update = ""

        cursor = database.database_opening.operator_db()
        id = ""
        cursor.execute("select p.id from peoples p where p.name = '" + termobusca + "' ")

        retorno = cursor.fetchone()

        for i in retorno:
            objeto = i
            id = objeto

        print(id)
        opcao = ""
        print("Atualizar:\n1-Nome\n2-E-mail\n3-Phone")
        print("....")
        opcao = input("Digite uma Opcao de Operacao: ")

        if opcao == '1':
            novo_nome = input('Digite o novo Nome: ')
            sql_update = "update peoples set name = '" + novo_nome + "' where id = "+str(id)+""

        elif opcao == '2':
            novo_email = input('Digite o e-mail: ')
            sql_update = "update peoples set email = '" + novo_email + "' where id = " + str(id)+""

        elif opcao == '3':
            novo_phone = input('Digite o phone: ')
            sql_update = "update peoples set phone = '" + novo_phone + "' where id = " + str(id)+""

        elif opcao == '1,2':
            novo_nome = input('Digite o novo Nome: ')
            novo_email = input('Digite o e-mail: ')
            sql_update = "update peoples set name = '" + novo_nome + "', email = "+ novo_email+"' where id = " + str(id)+""

        elif opcao == '1,3':
            novo_nome = input('Digite o novo Nome: ')
            novo_phone = input('Digite o phone: ')
            sql_update = "update peoples set name = '" + novo_nome + "', phone = '" + novo_phone + "' where id = " + str(
                id) + ""

        elif opcao == '2,3':
            novo_email = input('Digite o e-mail: ')
            novo_phone = input('Digite o phone: ')
            sql_update = "update peoples set email = '" + novo_email + "', phone = '" + novo_phone + "' where id = " + str(
                id) + ""


        cursor_update = database.database_opening.operator_db()
        cursor_update.execute(sql_update)
        #database.database_opening.operator_db().commit()
        print('Registro Atualizado com Sucesso!!!', termobusca)


def delete_people():
    db = credenciaisBanco
    termobusca = input("Digite o code:")

    cursor = database.database_opening.operator_db()
    id = ""
    cursor.execute("select p.id from peoples p where p.identify = " + termobusca + " ")

    retorno = cursor.fetchone()

    for i in retorno:
        objeto = i
        id = objeto

    cursor_update = db.cursor()
    cursor_update.execute("delete from peoples p where p.id = "+str(id)+"")
    #database.database_opening.operator_db().commit()

    print("*****Registro Excluido com Sucesso*********")


def add_people_on_work():
    db = credenciaisBanco
    #Informe Jobs
    termobusca = input("Digite o title da Job:")

    cursor = database.database_opening.operator_db()
    id = ""
    cursor.execute("select j.id from job j where j.title = '" + termobusca + "' ")
    retorno = cursor.fetchone()

    for i in retorno:
        objeto = i
        id = objeto

    #Informe People
    termobusca_people = input("Digite o code do Requerente: ")

    cursor = db.cursor()
    id_People = ""
    cursor.execute("select p.id from peoples p where p.id = " + termobusca_people + " ")
    retorno_people = cursor.fetchone()

    for i in retorno_people:
        objeto = i
        id_People = objeto

    cursor_update = db.cursor()
    cursor_update.execute("update peoples set job_id = "+str(id)+" where id = " + str(id_People) + "")
    #database.database_opening.operator_db().commit()


    print("*****Registro Atualizado com Sucesso*********")


def add_people_on_local():
    #db = credenciaisBanco
    #Informe Local
    termobusca = input("Digite o Postal Code da Location: ")

    cursor = database.database_opening.operator_db()
    id = ""
    cursor.execute("select l.id from location l where l.postal_code = " + termobusca + " ")
    retorno = cursor.fetchone()

    for i in retorno:
        objeto = i
        id = objeto

    #Informe People
    termobusca_people = input("Digite o code do Requerente:")

    cursor = database.database_opening.operator_db()
    id_People = ""
    cursor.execute("select p.id from peoples p where p.id = " + termobusca_people + " ")
    retorno_people = cursor.fetchone()

    for i in retorno_people:
        objeto = i
        id_People = objeto

    cursor_update = database.database_opening.operator_db()
    cursor_update.execute("update peoples set location_id = "+str(id)+" where id = " + str(id_People) + "")
    #database.database_opening.operator_db().commit()


    print("*****Registro Atualizado com Sucesso*********")
