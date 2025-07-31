import sqlite3  

def criar_conexao():
    """Cria uma conexão com o banco de dados SQLite."""
    conexao = sqlite3.connect('dados.db')
    return conexao