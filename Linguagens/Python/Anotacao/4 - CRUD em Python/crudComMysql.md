<img src="https://www.mysql.com/common/logos/logo-mysql-170x115.png" width="100" align="right" style="border-radius: 15px;">

# CRUD com MySQL

## 📦 Instalação de pacotes

Para instalar a biblioteca MySQL Connector, execute:

```sh
pip install mysql-connector-python
```

## 📥 Importar biblioteca para conectar

```python
import mysql.connector
```

## 🔌 Como conectar com MySQL

```python
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='nomeDoBanco',
)
```

## 🖱️ Cursor

O cursor é um objeto que permite interagir com o banco de dados, executando comandos SQL e obtendo os resultados.

```python
cursor = conexao.cursor()
```

## ❌ Finalizar o programa

Sempre ao finalizar o programa é necessário o fechamento do cursor e da conexão.

```python
cursor.close()
conexao.close()
```

## ➕ Create

Adicionar novos registros ao banco de dados.

```python
nome_produto = "chocolate"
valor = 15
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit()  # Confirma a edição no banco de dados
```

## 📖 Read

Consultar dados armazenados no banco de dados.

```python
comando = f'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall()  # Lê o banco de dados
print(resultado)
```

## 🔄 Update

Atualizar informações de registros existentes no banco de dados.

```python
nome_produto = "todynho"
valor = 6
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()  # Confirma a edição no banco de dados
```

## ❌ Delete

Remover registros do banco de dados.

```python
nome_produto = "todynho"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()  # Confirma a edição no banco de dados
```

## 🖥️ Código de exemplo

Código de CRUD que adiciona itens à tabela de vendas:

```python
import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='bdyoutube',
)
cursor = conexao.cursor()

# CREATE
nome_produto = "todynho"
valor = 8
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit()  # Confirma a edição no banco de dados

# READ
comando = f'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall()  # Lê o banco de dados
print(resultado)

# UPDATE
nome_produto = "todynho"
valor = 6
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()  # Confirma a edição no banco de dados

# DELETE
nome_produto = "todynho"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()  # Confirma a edição no banco de dados

cursor.close()
conexao.close()
```

# Fontes dos Estudos 📚🔍

- [CRUD em Python - Python e MySQL][1]
- [MySQL Installer][2]

[1]: https://www.youtube.com/watch?v=_q3j25ACmQ4
[2]: https://dev.mysql.com/downloads/installer/