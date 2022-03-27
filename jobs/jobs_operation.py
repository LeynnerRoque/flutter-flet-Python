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

def create_job():
    #opDB = credenciaisBanco
    #cursor = database.database_opening.operator_db()

    title = input("Digite o title do Job: ")
    salary = input("Digite a Remuneracao: ")
    enterprise = input("Digite o code da Empresa: ")

    cursor = database.database_opening.operator_db()
    id = ""
    cursor.execute("select e.id from enterprise e where e.identify = " + enterprise + " ")
    retorno = cursor.fetchone()

    for i in retorno:
        objeto = i
        id = objeto

    cursor.execute("insert into job (title,description,salry,enterprises_id) values('" + title + "','" + title + "'," + str(
            salary) + "," + str(id) +") ")

    #database.database_opening.operator_db().commit()

    print('*************Inserido com Sucesso************')


def update_jobs():
    #opDB = credenciaisBanco
    cursor = database.database_opening.operator_db()
    termo_busca = input("Digite o Title para operar: ")

    id = ""
    cursor.execute("select j.id from job j where j.title = '" + termo_busca + "' ")
    retorno = cursor.fetchone()

    for i in retorno:
        objeto = i
        id = objeto


    opcao = ""
    sql_update = ""

    print("Atualizar Job\n1 - Title do Job\n2 - Salary\n3 - Empresa")
    opcao = input("Opcao: ")

    if opcao == '1':
        novo_title = input("Digite o novo Title: ")
        sql_update = "update job set title = '"+novo_title+"' where id = "+str(id)
    elif opcao == '2':
        novo_salary = input("Digite o novo salary: ")
        sql_update = "update job set salry = '" + novo_salary + "' where id = " + str(id)
    elif opcao == '3':
        nova_empresa = input("Digite o identify da empresa: ")

        id_busca = ""
        cursor.execute("select e.id from enterprise e where e.identify = " + nova_empresa + " ")
        retorno_enterprise = cursor.fetchone()

        for i in retorno_enterprise:
            objeto = i
            id_busca = objeto

        sql_update = "update job set enterprises_id = '" + str(id_busca) + "' where id = " + str(id)


    cursor_update = database.database_opening.operator_db()
    cursor_update.execute(sql_update)
    #database.database_opening.operator_db().commit()

    print('*************Atualizado com Sucesso********************')

def add_job_on_enterprise():
    #opDB = credenciaisBanco
    cursor = database.database_opening.operator_db()
    termo_busca = input("Digite o Title para operar: ")

    id = ""
    cursor.execute("select j.id from job j where j.title = '" + termo_busca + "' ")
    retorno = cursor.fetchone()

    for i in retorno:
        objeto = i
        id = objeto

    opcao = ""
    sql_update = ""

    enterprise_add = input('Digite a Empresa: ')
    id_enterprise = ""
    cursor.execute("select e.id from enterprise e where e.foundation_name = '" + enterprise_add + "' ")
    resposta = cursor.fetchone()

    for i in resposta:
        objeto = i
        id_enterprise = objeto

    sql_update = "update job set enterprises_id = "+str(id_enterprise)+" where id = "+str(id)

    cursor_update = database.database_opening.operator_db()
    cursor_update.execute(sql_update)
    #database.database_opening.operator_db().commit()
    print('*************Atualizado com Sucesso********************')

def quantidadePorJob():
    #opDB = credenciaisBanco
    cursor = database.database_opening.operator_db()
    termo_busca = input("Digite o Title para operar: ")

    id = ""
    valores = []
    cursor.execute("select count(p.id), j.title from appjobs.peoples p, appjobs.job j, appjobs.enterprise e "
                   "where p.work_id = j.id "
                   "and j.enterprises_id = e.id "
                   "and e.foundation_name  = '" + termo_busca + "' group by j.id")
    retorno = cursor.fetchall()

    for i in retorno:
        objeto = i
        id = objeto
        valores.append(objeto)

    print(valores)

