import os
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
            
            elif idade < 0 or altura < 0.0 or peso < 0.0:
                st.error("Idade, altura e peso devem ser valores positivos.")
             
            else:
                pessoa = Pessoa(nome=nome, idade=idade, altura=altura, peso=peso)
                inserir_pessoa(pessoa)
                st.success(f"Pessoa {pessoa.nome} cadastrada com sucesso!")
            
elif menu == "consulta de Pessoas":
    st.title("Consulta de Pessoas")
    df = carregar_dados()
    st.dataframe(df)
    
elif menu == "Atualização de Pessoas":
    st.title("Atualização de Pessoas")
    df = carregar_dados()
    pessoa_id = st.selectbox("Selecione a pessoa para atualizar", df['id'])
    if pessoa_id:
        pessoa = selecionar_pessoa(pessoa_id)
        if pessoa:
            with st.form("atualizacao_pessoa"):
                novo_nome = st.text_input("Novo Nome", value=pessoa.nome)
                nova_idade = st.number_input("Nova Idade", min_value=0, max_value=120, value=pessoa.idade)
                nova_altura = st.number_input("Nova Altura (em metros)", min_value=0.0, format="%.2f", value=pessoa.altura)
                novo_peso = st.number_input("Novo Peso (em kg)", min_value=0.0, format="%.2f", value=pessoa.peso)
                if st.form_submit_button("Atualizar"):
                    if novo_nome == pessoa.nome and nova_idade == pessoa.idade and nova_altura == pessoa.altura and novo_peso == pessoa.peso:
                        st.warning("Nenhum dado foi alterado.")
                    else:
                        pessoa.nome = novo_nome
                        pessoa.idade = nova_idade
                        pessoa.altura = nova_altura
                        pessoa.peso = novo_peso
                        pessoa.id = pessoa_id
                        if atualizar_pessoa(pessoa):
                            st.success(f"Pessoa {pessoa.nome} atualizada com sucesso!")
                        else:
                            st.error("Erro ao atualizar a pessoa. Verifique os dados e tente novamente.")
                            

    



    

