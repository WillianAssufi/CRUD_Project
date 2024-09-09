import getpass
from database import crud

user_connection = str(input("\nDigite o nome de usuario para se conectar o Banco de Dados: "))
user_password = str(getpass.getpass("Digite sua senha: "))
dados = crud(user_connection, user_password)
print("Cadastro e Consulta de Usúarios!")
print("\nFaça login de Admin")

dados.Read_admin()

while True:
    operation = " "
    print("\n1 - Cadastrar Usuario\n2 - Consultar Base de Dados\n3 - Alterar Informação\n4 - Remover Usuario\n0 - Sair\n")

    while(operation != "0"):
        operation = str(input("Digite a operação que deseja realizar: "))

        if(operation == "1"): #CREATE
            print("Preencha os dados a seguir para cadastrar")
            firstname = input("\nPrimeiro Nome: ")
            lastname = input("\nSobrenome: ")
            email = input("\nEmail: ")
            password = input("\nSenha: ")
            birthday = input("\nDigite a data de aniversário(Somente números. Ex: 19991231): ")
            dados.Create(firstname, lastname, email, birthday, password)
            break
        
        elif(operation == "2"): #READ
            read_op = str(input("\nQue tipo de Consulta deseja realizar:\n1 - Por ID\n2 - Por Nome\n3 - Por Email\n4 - Exibir todos os Dados\nDigite a Opção: "))
            if(read_op == "1"):
                id = str(input('Digite o ID que deseja consultar: '))
                dados.Read("1", id)
                break
            elif(read_op == "2"):
                firstname = str(input('Digite o Nome que deseja consultar: '))
                dados.Read("2", firstname)
                break
            elif(read_op == "3"):
                email = str(input('Digite o Email que deseja consultar: '))
                dados.Read("3", email)
                break
            elif(read_op == "4"):
                dados.Read("4", None)
                break
        elif(operation == "3"): #UPDATE
            update_op = str(input("\nQual Informação deseja alterar:\n1 - Nome\n2 - Sobrenome\n3 - Email\n4 - Senha\n5 - Data de Nascimento\nDigite a Opção: "))
            id_confirm = str(input("\nConfirme o número de ID do usuário que deseja realizar a alteração: "))
            if(update_op == "1"):
                firstname = str(input("Digite o novo nome: "))
                dados.Update(id_confirm, update_op, firstname)
                break
            elif(update_op == "2"):
                lastname = str(input("Digite o novo sobrenome: "))
                dados.Update(id_confirm, update_op, lastname)
                break
            elif(update_op == "3"):
                email = str(input("Digite o novo email: "))
                dados.Update(id_confirm, update_op, email)
                break
            elif(update_op == "4"):
                password = str(input("Digite a nova senha: "))
                dados.Update(id_confirm, update_op, password)
                break
            elif(update_op == "5"):
                birthday = str(input("Digite a nova data de nascimento "))
                dados.Update(id_confirm, update_op, birthday)
                break
        elif(operation == "4"): #DELETE
            id_user = str(input("Digite o ID do usuario que deseja deletar: "))
            dados.Delete(id_user)
            break
            
        elif(operation == "0"):
            print("\nFechando...")
            dados.close()
            exit()
        else:
            print("\nOperação invalida, Tente Novamente!\n")
            
