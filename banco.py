import sqlite3
import pandas as pd

def carregar_dados():
    conn = sqlite3.connect('dados.db')
    df = pd.read_sql_query("SELECT * FROM pessoa", conn)    
    conn.close()
    return df