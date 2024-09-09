import mysql.connector
import getpass

class crud:
    def __init__(self, user, password):
        self.Connect_database(user, password)
    def Connect_database(self, user, password):
        connection = None
        try:
            self.cnnx = mysql.connector.connect(
                host = 'localhost',
                user = user,
                password = password,
                database = 'python_crud',
            )
            print("Conexão com o Banco de Dados bem sucessida!")
        except Exception as error: 
            print(f"Error: '{error}'")
            
        return connection
      
    def Create(self, firstname, lastname, email, birthday, password): #CREATE
        cursor = self.cnnx.cursor()
        
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.birthday = birthday
        
        comando = f'INSERT INTO crud (firstname, lastname, email, password, birthday) VALUES ("{self.firstname}", "{self.lastname}", "{self.email}", "{self.password}", "{self.birthday}")'
      
        cursor.execute(comando)
        self.cnnx.commit()
        print("\nDados inseridos com sucesso!")
        cursor.close()
        
    def Read(self, read_op, read_info): #READ
        cursor = self.cnnx.cursor()
        self.read_info = read_info
        self.read_op = read_op
        
        print("\nConsultando base de dados..\n")
        operations = {
            "1": 'SELECT * FROM crud WHERE id = {}', 
            "2": 'SELECT * FROM crud WHERE firstname = "{}"',
            "3": 'SELECT * FROM crud WHERE email = "{}"',
            "4": 'SELECT * FROM crud'
        }
        
        query = operations[self.read_op].format(self.read_info)
        print(query)
                           
        cursor.execute(query)
        result = cursor.fetchall() # Ler o banco de dados
        for x in result:
            x = list(x)
            x[5] = x[5].strftime("%d/%m/%Y")
            print(x)
        cursor.close()
        
    def Update(self, id, update_op, update_info): #UPDATE
        cursor = self.cnnx.cursor()
        self.id = id
        list = {"1":"firstname","2":"lastname","3":"email","4":"password","5":"birthday"}
        update_this = list[update_op]
        self.update_info = update_info
        
        comando = f'UPDATE crud SET {update_this} = "{update_info}" WHERE id = {self.id}'
                
        cursor.execute(comando)
        self.cnnx.commit()
        print("\nAlteração realizada com sucesso!")
        cursor.close()
        
    def Delete(self, id): #DELETE
        cursor = self.cnnx.cursor()
        self.id = id
        
        comando = f'DELETE FROM crud WHERE id = "{self.id}"'
        
        cursor.execute(comando)
        self.cnnx.commit()
        print("Dados deletados com sucesso!")
        cursor.close()

    def Read_admin(self):
        cursor = self.cnnx.cursor()
        
        psw = 1 
        
        read = 'SELECT * FROM admin'
        cursor.execute(read)
        result = cursor.fetchall()
        while psw == 1:
            for x in result:
                x = list(x)
                user = input(str("Digite seu Usuário: "))
                password = str(getpass.getpass("Digite sua Senha: "))
                if x[1] == user and x[2] == password:
                    psw = 0
                    print(f"Bem vindo {x[1]}")
                else:
                    print("\nLogin ou senha invalidos!\n")
            cursor.close()       
                
    def close(self):
        self.cnnx.close()
        
if __name__ == '__main__':
    crud
    
        
        


        