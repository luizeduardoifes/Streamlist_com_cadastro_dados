import streamlit as st
from banco import carregar_dados
from repo.pessoa_repo import *
criar_tabela_pessoa()

menu = st.radio("Menu", ["Cadastro de Pessoas","consulta de Pessoas", "Atualização de Pessoas", "Exclusão de Pessoas", "Listagem de Pessoas","sair"])

st.image("https://nfe.io/blog/app/uploads/2020/08/sistema-de-cadastro-clientes.jpg", caption="Cadastro de Pessoas")

if menu == "Cadastro de Pessoas":
    with st.form("cadastro_pessoa"):
        nome = st.text_input("Nome")
        idade = st.number_input("Idade", min_value=0, max_value=120)
        altura = st.number_input("Altura (em metros)", min_value=0.0, format="%.2f")
        peso = st.number_input("Peso (em kg)", min_value=0.0, format="%.2f")
        
        if st.form_submit_button("Cadastrar"):
            if not nome or idade <= 0 or altura <= 0.0 or peso <= 0.0:
                st.error("Por favor, preencha todos os campos corretamente.")
                
            elif nome.isdigit():
                st.error("O nome não pode ser apenas números.")
                
            elif nome == " ":
                st.error("O nome não pode ser vazio.")
            
            elif nome in carregar_dados()['nome'].values:
                st.error("Já existe uma pessoa cadastrada com esse nome.") 
            
            else:
                pessoa = Pessoa(nome=nome, idade=idade, altura=altura, peso=peso)
                inserir_pessoa(pessoa)
                st.success(f"Pessoa {pessoa.nome} cadastrada com sucesso!")
            
elif menu == "consulta de Pessoas":
    st.title("Consulta de Pessoas")
    df = carregar_dados()
    st.dataframe(df)


    

