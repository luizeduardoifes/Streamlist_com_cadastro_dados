from data.database import criar_conexao
from models.pessoa import Pessoa
from sql.pessoa_sql import *

def criar_tabela_pessoa():
    """Cria a tabela pessoa no banco de dados."""
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(CREATE_TABLE_PESSOA)
    conexao.commit()
    conexao.close()
    
def inserir_pessoa(pessoa: Pessoa) -> Pessoa:
    """Insere uma nova pessoa no banco de dados."""
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(INSERT_PESSOA, (pessoa.nome, pessoa.idade, pessoa.altura, pessoa.peso))
    conexao.commit()
    pessoa.id = cursor.lastrowid
    conexao.close()
    return pessoa

def selecionar_pessoa(id: int) -> Pessoa:
    """Seleciona uma pessoa pelo ID."""
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(SELECT_PESSOA, (id,))
    row = cursor.fetchone()
    conexao.close()
    
    if row:
        return Pessoa(nome=row[1], idade=row[2], altura=row[3], peso=row[4])
    return None 

def atualizar_pessoa(pessoa: Pessoa) -> bool:
    """Atualiza os dados de uma pessoa no banco de dados."""
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(UPDATE_PESSOA, (pessoa.nome, pessoa.idade, pessoa.altura, pessoa.peso, pessoa.id))
    conexao.commit()
    conexao.close()
    
    return cursor.rowcount > 0

def deletar_pessoa(id: int) -> bool:
    """Deleta uma pessoa pelo ID."""
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(DELETE_PESSOA, (id,))
    conexao.commit()
    conexao.close()
    
    return cursor.rowcount > 0

