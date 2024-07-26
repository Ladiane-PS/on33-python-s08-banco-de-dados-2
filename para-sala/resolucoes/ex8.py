#  **Escrita em CSV**: cria arquivo csv
#    - Escreva um script que crie um arquivo CSV chamado `funcionarios.csv` com as colunas `id`, `nome`, `departamento`.

import csv

funcionarios = [
       [1, 'Ana', 'Financeiro'],
       [2, 'Carlos', 'TI'],
       [3, 'Beatriz', 'RH'],
       [4, 'Ladiane', 'TI'],
       [5, 'Vando', 'Advogado'] 
    ]

with open('funcionarios.csv', 'w', newline='', encoding='utf-8') as csvfile: # w da a permisão de escrita
    escritor = csv.writer(csvfile)
    escritor.writerow(['id', 'nome', 'departamento']) # sempre tem qu emndar uma lista no caso id', 'nome', 'departamento'
    escritor.writerows(funcionarios) # sempre mandar lista no caso funcionarios

    # abertura de leitura e escrita

# writer escrever linas e writerows escrever varais linhas        