import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st
from datetime import datetime

# Autenticar a API do Google Sheets
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('formulario-online-limite-528c566e0588.json', scope)
client = gspread.authorize(creds)

# Abrir a planilha do Google Sheets e selecionar a tabela
sheet = client.open('base-de-dados').sheet1

# Definir os campos do formulário
nome = st.text_input('Nome')
email = st.text_input('E-mail')
telefone = st.text_input('Telefone')

# Verificar o limite de vagas
limite_vagas = 3
numero_inscricoes = len(sheet.get_all_values()) - 1
if numero_inscricoes >= limite_vagas:
    st.error('Vagas esgotadas!')
else:
    # Validar os campos do formulário
    if not nome:
        st.error('Por favor, informe seu nome.')
    elif not email:
        st.error('Por favor, informe seu e-mail.')
    elif not telefone:
        st.error('Por favor, informe seu telefone.')
    elif not email.endswith('@gmail.com'):
        st.error('Por favor, informe um e-mail válido do Gmail.')
    else:
        # Inserir os dados na tabela do Google Sheets
        data_inscricao = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        nova_inscricao = [nome, email, telefone, data_inscricao]
        sheet.append_row(nova_inscricao)

        # Exibir uma
