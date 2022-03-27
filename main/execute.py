import management._opMain as opMain
from enterprises import enterprise_operation as enterprise
from jobs import jobs_operation as job
from local import local_operation as local
from peoples import peoples_operation as people


opcao = ""

while opcao != 0:
    print('**********************************************')
    print('\t\tApp Jobs - Interface Python')
    print('**********************************************')
    print('\n')
    print('Menu de Opcoes:\n1 - Cadastro de Pessoas'
          '\n2 - Cadastro de Jobs'
          '\n3 - Cadastro de Enterprise'
          '\n4 - Cadastro de Locais')

    opcao = input('Digite com a Opcao: ')

    if opcao == '1':
        opcao_people = ''
        while opcao_people != '0':
            print('******************')
            print('\t\tPeoples')
            print('******************')

            print('\n1 - Novo\n2 - Atualizar\n3 - Adicionar Job\n4 - Adicionar Local\n5 - Buscar\n0 - Retornar')
            opcao_people = input('Entre com a Opcao: ')

            if opcao_people == '1':
                people.add_peoples()
            elif opcao_people == '2':
                people.update_peoples()
            elif opcao_people == '3':
                people.add_people_on_work()
            elif opcao_people == '4':
                people.add_people_on_local()
            elif opcao_people == '5':
                people.select_all_peoples()
            elif opcao_people == '0':
                break

    if opcao == '2':
        opcao_job = ''
        while opcao_job != '0':
            print('******************')
            print('\t\tJobs')
            print('******************')

            print('\n1 - Novo'
                  '\n2 - Atualizar'
                  '\n3 - Adicionar Job on Enterprise'
                  '\n4 - Buscar Jobs'
                  '\n0 - Retornar')
            opcao_job = input('Entre com a Opcao: ')

            if opcao_job == '1':
                job.create_job()
            elif opcao_job == '2':
                job.update_job()
            elif opcao_job == '3':
                job.add_job_enterprise()
            elif opcao_job == '4':
                job.select_all_jobs()
            if opcao_job == '0':
                break
    elif opcao == '3':
        opcao_enterprise = ''
        while opcao_enterprise != '0':
            print('******************')
            print('\t\tEnterprises')
            print('******************')

            print('\n1 - Novo'
                  '\n2 - Atualizar'
                  '\n3 - Buscar Enterprise'
                  '\n4 - Quantidade de Peoples in Jobs'
                  '\n0 - Retornar')
            opcao_enterprise = input('Entre com a Opcao: ')

            if opcao_enterprise == '1':
                enterprise.create_enterprise()
            elif opcao_enterprise == '2':
                enterprise.update_enterprise()
            elif opcao_enterprise == '3':
                print(enterprise.select_all())
            elif opcao_enterprise == '4':
                enterprise.quantidadePeoplesInJobs()
            if opcao_enterprise == '0':
                 break
    elif opcao == '4':
        opcao_local = ''
        while opcao_local != '0':
            print('******************')
            print('\t\tLocations')
            print('******************')

            print('\n1 - Novo\n2 - Atualizar\n3 - Buscar Local\n0 - Retornar')
            opcao_local = input('Entre com a Opcao: ')

            if opcao_local == '1':
                enterprise.create_enterprise()
            elif opcao_local == '2':
                enterprise.update_enterprise()
            elif opcao_local == '3':
                enterprise.select_all_enterprise()
            if opcao_local == '0':
                break

    if opcao == '0':
        print('********************************')
        print('\t\tSistema Finalizado')
        print('********************************')
        exit()