import database

class Main:
    def __init__(self):
        self.db = database.Database()
        self.show()
        self.acessUser()
        self.db.close()

    def show(self):
        print('              --------------------------\
            \n             ---____----____----_----_---\
            \n            ---|    \--|    \--| \  / |---\
            \n           ----|  _ /--|   _/--|  \/  |----\
            \n          -----| |-----| |-----| |\/| |-----\
            \n         ------|_|-----|_|-----|_|  |_|------\
            \n        --------------------------------------\
            \n       --------Portable-Password-Manager-------\n')
    
    def createUser(self):
        print('\nCRIANDO NOVO USUÁRIO:')
        nome = input('Digite o nome do usuário: ')
        senha = input('Digite a senha master desse usuário: ')
        idNewUser = self.db.createUser(nome, senha)
        self.acessUser()

    def acessUser(self):
        print('\nLISTA DE USUÁRIOS:\n0 - Para criar um novo usuário')
        listUsers = self.db.select('usuarios', order='nome')
        count = 0
        for user in listUsers:
            count += 1
            print('{0} - {1}'.format(count, user[1]))
        numUser = input('\nDigite o número correspondente: ')
        if numUser == str(0):
            self.createUser()
        else:
            try:
                inUser = listUsers[int(numUser) - 1]
            except:
                print('Número digitado incorretamente!')
                self.acessUser()
            print('Usuário', inUser[1])
            passEmpty = True
            while passEmpty:
                passMaster = input('\nDigite a senha: ')
                if passMaster == inUser[2]:
                    passEmpty = False
                    self.acessConta(inUser[0], inUser[1])
                elif(passMaster == str(0)):
                    passEmpty = False
                    self.acessUser()
                else:
                    print('Senha incorreta! Digite 0 se preferir voltar')

    def createConta(self, idUser, nomeUser):
        print('\nCRIANDO NOVA CONTA EM USUÁRIO {}:'.format(nomeUser))
        nome_site = input('Digite o nome do site: ')
        email = input('Email ou username de acesso ao site {}: '.format(nome_site))
        senha = input('Digite a senha de acesso ao site {}: '.format(nome_site))
        url = input('Digite o endereço URL do site {} (opcional): '.format(nome_site))
        idNewConta = self.db.createConta(idUser, email, senha, nome_site, url)
        self.acessConta(idUser, nomeUser)
    
    def acessConta(self, idUser, nomeUser):
        listContas = self.db.select('contas', 'id_usuario == {}'.format(idUser), 'nome_site')
        print('\nLISTA DE CONTAS DO USUÁRIO {}:\n0 - Para criar uma nova conta'.format(nomeUser))
        count = 0
        for conta in listContas:
            count += 1
            print('{0} - {1} ({2})'.format(count, conta[4], conta[2]))
        numConta = input('\nDigite o número correspondente: ')
        if numConta == str(0):
            self.createConta(idUser, nomeUser)
        else:
            try:
                inConta = listContas[int(numConta) - 1]
            except:
                print('Número digitado incorretamente!')
                self.acessConta(idUser, nomeUser)
            print('\nSite: {0} ({1})\nEmail/Username: {2}\nSenha: {3}'
            .format(inConta[4], inConta[5], inConta[2], inConta[3]))
            result = input('\nDigite 0 para voltar ou qualquer outra tecla para sair: ')
            if result == str(0):
                self.acessConta(idUser, nomeUser)
            else:
                print('Tchau!!!')
Main()