# **Criação de Banco de Dados e Tabelas**:
import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor() # atraves do curso vamos usar  o metodo execute, curso espera uma informação de entrada
# varias """ qundo para executar mais de uma linha "
cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
       id INTEGER PRIMARY KEY AUTOINCREMENT,   
       nome TEXT NOT NULL,
       idade INTEGER NOT NULL
   )
   """)

conn.commit()  # commit igual  do git hub
cursor.close() # fecha
conn.close()  # fechar conexão
# not exists verifica se a tabela existe , caso tenha não fazer novamente
# autoincrement para colocar os números na ordem
# o null para não deixa a linha nulo e  obrigar a a colocar valor 
