import sqlite3

# Caminho para seu banco de dados
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Nome da tabela que deseja limpar
nome_tabela = 'Notes'

# Apaga todos os dados da tabela
cursor.execute(f'DELETE FROM Notes')
conn.commit()

print(f'Todos os dados da tabela "{nome_tabela}" foram apagados.')

# Fecha a conexão
conn.close()
