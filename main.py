import sqlite3

# conectando...
conn = sqlite3.connect('data.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
'''
cursor.execute("""
CREATE TABLE usuario (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        email VARCHAR(150) NOT NULL,
        senha VARCHAR(200) NOT NULL,
        nome_site VARCHAR(60) NOT NULL,
        url VARCHAR(301)
);
""")

cursor.execute("""
INSERT INTO usuario (email, senha, nome_site, url)
VALUES ('fulano@google.com', 'm3nk2n3', 'Google', 'google.com')
""")
'''
cursor.execute("""
SELECT * FROM usuario;
""")
for linha in cursor.fetchall():
    print(linha)
# desconectando...
conn.close()


print('              --------------------------\
    \n             ---____----____----_----_---\
    \n            ---|    \--|    \--| \  / |---\
    \n           ----|  _ /--|   _/--|  \/  |----\
    \n          -----| |-----| |-----| |\/| |-----\
    \n         ------|_|-----|_|-----|_|  |_|------\
    \n        --------------------------------------\
    \n       --------Portable-Password-Manager-------\n')
print('LISTA DE USUÁRIOS:\n0 Para novo usuário\n1 Cicrano\n2 Zé')
value = input('Digite o número referente ao usuário: ')
print(value)