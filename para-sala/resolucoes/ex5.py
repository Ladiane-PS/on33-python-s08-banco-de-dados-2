#**Remoção de Dados**:
import sqlite3
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM estudantes WHERE nome = ?", ('Charlie',))

conn.commit()
cursor.close()
conn.close()

# A vírgula após 'Charlie' é necessária para criar uma tupla com um único elemento.
# Isso garante que o método execute interprete corretamente o argumento como uma sequência,
# permitindo que a consulta SQL funcione corretamente