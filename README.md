![sqliteepython](https://github.com/user-attachments/assets/a8a237a3-326e-481f-9086-bcbe7bcbb4de)


# Integração de CSV com SQLite usando Python

Este projeto demonstra como integrar dados de arquivos CSV com um banco de dados SQLite utilizando Python. O objetivo é criar um banco de dados, importar dados de um arquivo CSV para uma tabela, realizar operações CRUD (Create, Read, Update, Delete) e exportar os dados de volta para um novo arquivo CSV.

## Estrutura do Projeto

O projeto contém os seguintes arquivos:

1. **`criar_banco.py`**: Script para criar o banco de dados SQLite e a tabela `livros`.
2. **`importar_csv.py`**: Script para importar dados do arquivo `livros.csv` para a tabela `livros`.
3. **`consultar_livros.py`**: Script para consultar e exibir todos os registros da tabela `livros`.
4. **`atualizar_livro.py`**: Script para atualizar o preço de um livro específico na tabela `livros`.
5. **`remover_livro.py`**: Script para remover um livro específico da tabela `livros`.
6. **`exportar_csv.py`**: Script para exportar os dados da tabela `livros` para um novo arquivo CSV chamado `exportados_livros.csv`.
7. **`livros.csv`**: Arquivo CSV contendo dados de exemplo para a tabela `livros`.

## Pré-requisitos

Certifique-se de ter o Python instalado em seu sistema. Este projeto foi testado com Python 3.x.

Você também precisará da biblioteca `sqlite3`, que é incluída por padrão com Python, e a biblioteca `csv` para manipulação de arquivos CSV.

