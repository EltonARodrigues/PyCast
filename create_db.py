import sqlite3

conn = sqlite3.connect('feed.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE feed (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        url INTEGER
);
""")

print('Tabela criada com sucesso.')
# desconectando...
conn.close()
