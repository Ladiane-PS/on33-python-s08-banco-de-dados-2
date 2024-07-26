# **Atualização de Dados**:
import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

estudantes = [
       (25, 'Alice'),
       (26, 'Bob'),
]
cursor.executemany("UPDATE estudantes SET idade = ? WHERE nome = ? ", estudantes)
#mais de uma informação colocar o executemany

conn.commit()
cursor.close()
conn.close()