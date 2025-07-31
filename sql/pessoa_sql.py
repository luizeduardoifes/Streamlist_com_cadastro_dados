CREATE_TABLE_PESSOA = """
CREATE TABLE IF NOT EXISTS pessoa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    altura REAL NOT NULL,
    peso REAL NOT NULL
);
"""

INSERT_PESSOA = """
INSERT INTO pessoa (nome, idade, altura, peso) VALUES (?, ?, ?, ?);
"""

SELECT_PESSOA = """
SELECT id, nome, idade, altura, peso FROM pessoa WHERE id = ?;
"""

UPDATE_PESSOA = """
UPDATE pessoa SET nome = ?, idade = ?, altura = ?, peso = ? WHERE id = ?;
""" 

DELETE_PESSOA = """
DELETE FROM pessoa WHERE id = ?;
"""