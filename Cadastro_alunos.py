import pandas as pd

def cadastrar_dado():
    # Coletar informações do usuário
    ra = input("Digite o Registro Acadêmico: ")
    nome = input("Digite o nome do aluno: ")
    idade = input("Digite a idade: ")
    data_nascimento = input("Digite a data de nascimento (no formato DD/MM/AAAA): ")
    genero = input("Digite o gênero do aluno: ")
    endereco = input("Digite o endereço: ")
    cidade = input("Digite a cidade: ")
    cep = input("Digite o CEP: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    responsavel = input("Digite o nome do responsável: ")
    serie = input("Digite a série: ")
    sala = input("Digite a sala: ")
    periodo = input("Digite o período: ")

    # Verificar se o arquivo de dados existe
    if not df_exists('dados.csv'):
        # Criar um DataFrame vazio
        df = pd.DataFrame(columns=['ID', 'Registro Acadêmico', 'Nome do Aluno', 'Idade', 'Data de Nascimento', 'Gênero', 'Endereço', 'Cidade', 'CEP', 'Telefone', 'Email', 'Responsável', 'Série', 'Sala', 'Período'])
    else:
        # Carregar os dados existentes do arquivo CSV
        df = pd.read_csv('dados.csv')

    # Verificar o último ID utilizado
    last_id = get_last_id()

    # Gerar o próximo ID incrementando o último ID utilizado
    id = last_id + 1

    # Criar um novo registro como um dicionário
    novo_registro = {'ID': id, 'Registro Acadêmico': ra, 'Nome do Aluno': nome, 'Idade': idade, 'Data de Nascimento': data_nascimento,
                     'Gênero': genero, 'Endereço': endereco, 'Cidade': cidade, 'CEP': cep, 'Telefone': telefone, 'Email': email,
                     'Responsável': responsavel, 'Série': serie, 'Sala': sala, 'Período': periodo}

    # Adicionar o novo registro ao DataFrame 
    df.loc[len(df)] = novo_registro

    # Salvar o DataFrame em um arquivo CSV
    df.to_csv('dados.csv', index=False)

    print("Dados cadastrados com sucesso!")

def get_last_id():
    # Verificar se o arquivo de dados existe
    if not df_exists('dados.csv'):
        return 0

    # Carregar os dados do arquivo CSV para um DataFrame
    df = pd.read_csv('dados.csv')

    # Verificar o último ID utilizado
    last_id = df['ID'].max()

    return last_id if pd.notna(last_id) else 0

def df_exists(file_name):
    try:
        pd.read_csv(file_name)
        return True
    except FileNotFoundError:
        return False

# Programa principal
cadastrar_dado()
