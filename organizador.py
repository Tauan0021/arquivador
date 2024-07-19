import streamlit as st
import os

# Função para organizar arquivos
def organize_directory(full_path):
    os.chdir(full_path)

    # Cria uma lista com todos os arquivos "não diretórios" da pasta
    full_list = os.listdir()
    files_list = []
    for file in full_list:
        if not os.path.isdir(file):
            files_list.append(file)

    # Fazer uma varredura sobre todos os arquivos
    # Criar uma pasta para cada tipo de arquivo encontrado
    types = []
    for i in files_list:
        type_ = i.split('.')[-1].lower()
        if type_ not in types:
            types.append(type_)
            os.mkdir(type_)

    # Move todos os arquivos para as pastas correspondentes
    for file in files_list:
        file_type = file.split('.')[-1]
        path_to = os.path.join(file_type, file)
        os.replace(file, path_to)
        
def dezorganize_directory(full_path):
    folder_list = []
    for i in os.listdir():
        if os.path.isdir(i):
            folder_list.append(i)

    # Extrair arquivos das pastas
    for folder in folder_list:
        files = os.listdir(folder)
        for file in files:
            path_from = os.path.join(folder, file)
            os.replace(path_from, file)
        os.rmdir(folder)


# Configuração do app Streamlit
st.title("Organizador e Dezorganizador de Arquivos")

# Entrada do usuário para o nome do diretório
directory = st.text_input("Insira o caminho do diretório que deseja organizar:")

if st.button("Organizar"):
    if os.path.exists(directory) and os.path.isdir(directory):
        organize_directory(directory)
        st.success(f"O diretório '{directory}' foi organizado com sucesso!")
    else:
        st.error("O caminho inserido não é válido ou não é um diretório.")
        
directory = st.text_input("Insira o caminho do diretório que deseja dezorganizar:")

if st.button("Dezorganizar"):
    if os.path.exists(directory) and os.path.isdir(directory):
        dezorganize_directory(directory)
        st.success(f"O diretório '{directory}' foi dezorganizado com sucesso!")
    else:
        st.error("O caminho inserido não é válido ou não é um diretório.")
