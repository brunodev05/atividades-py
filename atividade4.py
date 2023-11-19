import sqlite3
from datetime import datetime

def conectar_banco():
    # Conectar ao banco de dados (o arquivo BancoPy.db será criado se não existir)
    conexao = sqlite3.connect("BancoPy.db")
    cursor = conexao.cursor()

    # Criar a tabela se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS funcionarios (
            Nome VARCHAR(50),
            Endereco VARCHAR(50),
            DataNascimento DATE,
            Salario REAL,
            CPF VARCHAR(14) PRIMARY KEY
        )
    ''')

    conexao.commit()
    return conexao, cursor

def cadastrar():
    conexao, cursor = conectar_banco()

    # Pedir ao usuário para inserir dados
    nome = input("Digite o nome: ")
    endereco = input("Digite o endereço: ")
    data_nascimento_str = input("Digite a data de nascimento (formato YYYY-MM-DD): ")
    salario = float(input("Digite o salário: "))
    cpf = input("Digite o CPF: ")

    # Verificar se o CPF já existe
    cursor.execute("SELECT * FROM funcionarios WHERE CPF=?", (cpf,))
    if cursor.fetchone() is not None:
        print("Erro: CPF já existe no banco de dados.")
    else:
        # Inserir dados no banco de dados
        data_nascimento = datetime.strptime(data_nascimento_str, "%Y-%m-%d").date()
        cursor.execute("INSERT INTO funcionarios VALUES (?, ?, ?, ?, ?)",
                       (nome, endereco, data_nascimento, salario, cpf))
        conexao.commit()
        print("Cadastro realizado com sucesso.")

    conexao.close()

def alterar():
    conexao, cursor = conectar_banco()

    # Pedir ao usuário para inserir o CPF a ser alterado
    cpf_alterar = input("Digite o CPF a ser alterado: ")

    # Verificar se o CPF existe
    cursor.execute("SELECT * FROM funcionarios WHERE CPF=?", (cpf_alterar,))
    dados_funcionario = cursor.fetchone()

    if dados_funcionario is not None:
        # Pedir ao usuário para inserir os novos dados
        nome = input("Digite o novo nome: ")
        endereco = input("Digite o novo endereço: ")
        data_nascimento_str = input("Digite a nova data de nascimento (formato YYYY-MM-DD): ")
        salario = float(input("Digite o novo salário: "))

        # Atualizar os dados no banco de dados
        data_nascimento = datetime.strptime(data_nascimento_str, "%Y-%m-%d").date()
        cursor.execute("UPDATE funcionarios SET Nome=?, Endereco=?, DataNascimento=?, Salario=? WHERE CPF=?",
                       (nome, endereco, data_nascimento, salario, cpf_alterar))
        conexao.commit()
        print("Dados alterados com sucesso.")
    else:
        print("Erro: CPF não encontrado no banco de dados.")

    conexao.close()

def excluir():
    conexao, cursor = conectar_banco()

    # Pedir ao usuário para inserir o CPF a ser excluído
    cpf_excluir = input("Digite o CPF a ser excluído: ")

    # Verificar se o CPF existe
    cursor.execute("SELECT * FROM funcionarios WHERE CPF=?", (cpf_excluir,))
    dados_funcionario = cursor.fetchone()

    if dados_funcionario is not None:
        # Excluir os dados do banco de dados
        cursor.execute("DELETE FROM funcionarios WHERE CPF=?", (cpf_excluir,))
        conexao.commit()
        print("Dados excluídos com sucesso.")
    else:
        print("Erro: CPF não encontrado no banco de dados.")

    conexao.close()

def menu():
    while True:
        print("\nMenu:")
        print("1. Cadastrar")
        print("2. Alterar")
        print("3. Excluir")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            alterar()
        elif opcao == "3":
            excluir()
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
