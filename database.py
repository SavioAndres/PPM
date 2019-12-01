import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor() 
        try:
            self.createTables()
        except:
            pass

    def createTables(self):
        self.cursor.execute("""
            CREATE TABLE usuarios (
                id Integer PRIMARY KEY  NOT NULL,
                nome Varchar(150)  NOT NULL,
                senha Varchar(120)  NOT NULL
            );
        """)
        self.cursor.execute("""
            CREATE TABLE contas (
                id Integer Primary Key Autoincrement  NOT NULL,
                id_usuario Integer  NOT NULL,
                email_user Varchar(300)  NOT NULL,
                senha Varchar(200)  NOT NULL,
                nome_site Varchar(60) NOT NULL,
                url Varchar(350),
                FOREIGN KEY(id_usuario) REFERENCES usuarios(id)
            );
        """)

    def createUser(self, nome, senha):
        self.cursor.execute("""
            INSERT INTO usuarios (nome, senha)
            VALUES ('{0}', '{1}')
        """.format(nome, senha))
        self.conn.commit()
        return self.cursor.lastrowid

    def createConta(self, id_usuario, email_user, senha, nome_site = '', url = ''):
        self.cursor.execute("""
            INSERT INTO contas (id_usuario, email_user, senha, nome_site, url)
            VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')
        """.format(id_usuario, email_user, senha, nome_site, url))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def select(self, table, where = '', order = ''):
        if not where == '': where = 'WHERE ' + where
        if not order == '': order = 'ORDER BY LOWER(' + order + ')'
        self.cursor.execute("SELECT * FROM {0} {1} {2}".format(table, where, order))
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()