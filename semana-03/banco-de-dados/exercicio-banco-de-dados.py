"""1.Crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro),nome(texto), idade(inteiro) e curso(texto)."""

import sqlite3

conexao = sqlite3.connect("atividade")
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')

"""2.Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior. """

# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1212,"Paula",20, "Engenharia")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1213,"Mariana",22, "Economia")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1214,"Carlos",28, "Direito")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1215,"Ana",21, "Ciência de dados")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1216,"Pedro",25, "Psicologia")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1217,"Rafaela",25, "Biologia")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1218,"Jorge",31, "Administração")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1219,"Luiza",18, "Medicina")')

"""3.Consultas Básicas: Escreva consultas SQL para realizar as seguintes tarefas:
a)Selecionar todos os registros da tabela "alunos"."""
# consulta = cursor.execute('SELECT * FROM alunos')

"""b)Selecionar o nome e a idade dos alunos com mais de 20 anos."""
# consulta = cursor.execute('SELECT nome,idade FROM alunos WHERE idade>20')

"""c)Selecionar os alunos do curso de "Engenharia" em ordem alfabética."""
# consulta = cursor.execute('SELECT * FROM alunos WHERE curso="Engenharia" ORDER BY nome')

# Consulta para as letras a), b) e c).
# for alunos in consulta:
#  print(alunos)

"""d)Contar o número total de alunos na tabela."""
# cursor.execute('SELECT COUNT(*) FROM alunos')
# consulta = cursor.fetchone()[0]
# print(f'O número total de alunos na tabela é {consulta}.')

"""4.Atualização e Remoção: 
a)Atualize a idade de um aluno específico na tabela."""
# Atualizando dados da aluna Mariana

# cursor.execute('UPDATE alunos SET curso="Administração" WHERE nome="Mariana"')

"""b)Remova um aluno pelo seu ID."""
# Removendo Pedro pelo ID.
# cursor.execute('DELETE FROM alunos WHERE id=1216')

"""5.Criar uma Tabela e Inserir Dados: Crie uma tabela chamada "clientes" com os campos: id(chaveprimária), nome(texto), idade(inteiro) e saldo(float).Insira alguns registros de clientes na tabela."""

# cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT)')

# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(11,"Kaya",35, 3500)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(21,"Priya",29, 5200)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(31,"Peter",41, 10000)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(41,"Thomas",21, 1200)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(51,"Ikaro",22, 4700)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(61,"Bea",26, 7400)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(71,"Eric",37, 12060)')

"""6.Consultas e Funções Agregadas: Escreva consultas SQL para realizar as seguintes tarefas:
a)Selecione o nome e a idade dos clientes com idade superior a 30anos."""

# consulta = cursor.execute('SELECT nome,idade FROM clientes WHERE idade>30')
# for clientes in consulta:
# print(clientes)

"""b)Calcule o saldo médio dos clientes."""
# cursor.execute('SELECT saldo FROM clientes')
# saldos = cursor.fetchall()

# if saldos:
#  saldos = [saldo[0] for saldo in saldos] #extração dos valores da
#  saldo_total = sum(saldos)
#  saldo_med = saldo_total/len(saldos)
#  print(f'O saldo médio dos clientes é R${saldo_med:.2f}.')
# else:
#  print('Nenhum saldo encontrado.')

"""c)Encontre o cliente com o saldo máximo."""
# consulta = cursor.execute('SELECT nome FROM clientes ORDER BY saldo DESC LIMIT 1')
# for clientes in consulta:
# print(clientes)

"""d)Conte quantos clientes têm saldo acima de 1000."""
# cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo>1000')
# consulta = cursor.fetchone()[0]
# print(f'O número total de clientes com saldo superior a 1000 reais é {consulta}.')

"""7. Atualização e Remoção com Condições:
a)Atualize o saldo de um cliente específico."""
# Atualizando o saldo da Kaya
# cursor.execute('UPDATE clientes SET saldo=5000 WHERE nome="Kaya"')

"""b)Remova um cliente pelo seuID."""
# Removendo Ikaro pelo id.
# cursor.execute('DELETE FROM clientes WHERE id=51')

"""8. Junção de Tabelas: Crie uma segunda tabela chamada "compras" com os campos: id(chaveprimária), cliente_id(chave estrangeira referenciando o id da tabela "clientes"), produto(texto) e valor(real). Insira algumas compras associadas a clientes existentes na tabela "clientes".Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra."""

# cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, cliente_id INT , produto VARCHAR(100), valor REAL, FOREIGN KEY(cliente_id) references clientes(id))')

# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(01, 11, "kindle", 300)')
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(02, 21, "celular", 1500)')
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(03, 31,"Smart Tv", 3000)')
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(04, 41,"Mouse", 30)')
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(05, 51,"Fone de ouvido", 80)')

# cursor.execute('UPDATE compras SET produto="Celular" WHERE id=02')
# cursor.execute('UPDATE compras SET produto="Kindle" WHERE id=01')

consulta = cursor.execute(
    "SELECT nome,produto,valor FROM clientes INNER JOIN compras on clientes.id=cliente_id"
)
for clientes in consulta:
    print(clientes)

# Cliente Ikaro não é apresentado na consulta acima pois foi excluído em uma das questões anteriores

conexao.commit()
conexao.close
