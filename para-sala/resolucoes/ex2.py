#**Inserção de Dados**:
import sqlite3
conn = sqlite3.connect('escola.db') # conn é uma variavel poderia ser conexao e mais utilizado conn
cursor = conn.cursor()

estudantes = [
       ('Alice', 21),
       ('Bob', 22),
       ('Charlie', 23)
   ]

cursor.executemany("INSERT INTO estudantes (nome, idade) VALUES (?, ?)", estudantes)
# executmay coloca mais de uma informação no insert de uma vez
conn.commit()
cursor.close()
conn.close()