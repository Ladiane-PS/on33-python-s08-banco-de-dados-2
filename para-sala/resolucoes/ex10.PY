# 10. **Exportação de SQLite para CSV**:
#     - Escreva um script que exporte os dados da tabela `clientes` do banco de dados `empresa.db` para um arquivo CSV chamado `exportados_clientes.csv`.
import csv
import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM clientes")
dados = cursor.fetchall()   #fetchall busca oo que esta no select e guarda em dados

with open('exportados_clientes.csv', 'w', newline='', 
encoding='utf-8') as csvfile:
        escritor = csv.writer(csvfile) #defip onde vai ser escrita 
        escritor.writerow(['id', 'nome', 'email'])
        escritor.writerows(dados)

#conn.commit()  nesse caso não precisa usar o commit o select não precisa usar o commit 
cursor.close()
conn.close()

# conn.commit(): Confirma as alterações feitas na transação atual e salva essas alterações no banco de dados.
# Sem commit(): As alterações são temporárias e podem ser revertidas se não forem confirmadas.
# Usar conn.commit() é uma prática essencial para garantir que suas mudanças no banco de dados sejam persistentes e seguras.