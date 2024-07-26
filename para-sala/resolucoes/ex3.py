#**Consulta de Dados**:
import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM estudantes") # ""  quando e para executar uma liha
registros = cursor.fetchall() # fetchall=buscar e for devolve linjha por linha 
# o cursor fetxhal pega o cursor execute de cima 

for registro in registros:
       print(registro)

cursor.close()
conn.close()

# As aspas triplas (""") em Python são usadas para definir strings que podem ocupar várias linhas.
# Elas são especialmente úteis para escrever textos longos, como docstrings ou consultas SQL complexas,
# sem a necessidade de usar caracteres de escape ou concatenar várias strings.
# O uso de aspas triplas é uma prática comum em Python, especialmente ao trabalhar com SQL ou textos longos, 
# pois melhora a clareza e a manutenção do código.

# Se você usasse aspas simples ou duplas, teria que usar o caractere de escape \n para indicar quebras de linha, o que tornaria o código menos legível:
# python
# cursor.execute("CREATE TABLE IF NOT EXISTS estudantes (\n"
#                "id INTEGER PRIMARY KEY AUTOINCREMENT,\n"
#                "nome TEXT NOT NULL,\n"
#                "idade INTEGER NOT NULL\n"
#                ")")