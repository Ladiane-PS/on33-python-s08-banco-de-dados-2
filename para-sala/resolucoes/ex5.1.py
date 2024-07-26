#**Remoção de Dados**: mais de um
import sqlite3
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

estudantes = [
       (1,),
       (2,),
]
cursor.executemany("DELETE FROM estudantes SET idade = ? WHERE id = ? ", estudantes)
# nesse caso e bom usar o id pois se tiver várias alice por exemplo ele apagaria todos os nome alice 


conn.commit()
cursor.close()
conn.close()
