import sqlalchemy

engine = sqlalchemy.create_engine("sqlite:///server.db")
connection = engine.connect()

connection.execute("""CREATE TABLE IF NOT EXISTS FUNCIONARIO (
 ID int not null,
 NOME varchar(255) not null,
 IDADE int not null,
 SALARIO float not null)
 """)

# Inserir um registro na tabela
connection.execute("INSERT INTO FUNCIONARIO VALUES (1, 'Paulo', 30, 2000.00)")
# Inserir dados informados pelo usuário
id_func = int(input("Id: "))
nome = input("Nome: ")
idade = int(input("Idade: "))
salario = float(input("Salário: "))
connection.execute("""INSERT INTO FUNCIONARIO VALUES ({}, '{}', {}, {})""".format(id_func, nome,
idade, salario))

result = connection.execute("SELECT * FROM FUNCIONARIO ORDER BY ID")
for linha in result:
 print(linha)

connection.execute("UPDATE FUNCIONARIO SET NOME='João Silva' where id=2")

connection.execute("DELETE FROM FUNCIONARIO WHERE ID=2")
connection.close()
