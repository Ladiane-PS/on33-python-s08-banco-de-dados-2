
# **Atualização de Dados**:
import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute("UPDATE estudantes SET idade = ? WHERE nome = ?", (23, 'Bob'))
#mais de uma informação colocar o executemany

conn.commit()
cursor.close()
conn.close()