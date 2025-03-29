#QUESTÃO 4 de 4 - Conteúdo até aula 06 

#Enunciado: Você e sua equipe de programadores foram contratados por pequena empresa 
# para desenvolver o software de gerenciamento de livros. 
# Este software deve ter o seguinte menu e opções: 

#Cadastrar Livro 
#Consultar Livro 
#Consultar Todos  
#Consultar por Id 
#Consultar por Autor 
#Retornar ao menu 
#Remover Livro 
#Encerrar Programa 

#Elabore um programa em Python que:  
#Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome [EXIGÊNCIA DE CÓDIGO 1 de 8]; 
#Deve-se implementar uma lista vazia com o nome de lista_livro e a variável id_global com valor inicial igual a 0 [EXIGÊNCIA DE CÓDIGO 2 de 8]; 
#Deve-se implementar uma função chamada cadastrar_livro(id) em que: [EXIGÊNCIA DE CÓDIGO 3 de 8]; 
#Pergunta nome, autor, editora do livro; 
#Armazena o id (este é fornecido via parâmetro da função), nome, autor, editora dentro de um dicionário; 
#Copiar o dicionário para dentro da lista_livro; 
#Deve-se implementar uma função chamada consultar_livro() em que: [EXIGÊNCIA DE CÓDIGO 4 de 8]; 
#Deve-se perguntar qual opção deseja (1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Autor / 4. Retornar ao menu): 
#Se Consultar Todos, apresentar todos os livros com todos os seus dados cadastrados; 
#Se Consultar por Id, apresentar o livro específico com todos os seus dados cadastrados; 
#Se Consultar por Autor, apresentar o(s) livro(s) do autor com todos os seus dados cadastrados; 
#Se Retornar ao menu, deve-se retornar ao menu principal; 
#Se Entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida" e repetir a pergunta D.a. 
#Enquanto o usuário não escolher a opção 4, o menu consultar livros deve se repetir. 
#Deve-se implementar uma função chamada remover_livro() em que: [EXIGÊNCIA DE CÓDIGO 5 de 8]; 
#Deve-se pergunta pelo id do livro a ser removido; 
#Remover o livro da lista_livro; 
#Se o id fornecido não for de um livro da lista, printar “Id inválido” e repetir a pergunta E.a. 
#Deve-se implementar uma estrutura de menu no código principal (main), ou seja, não pode estar dentro de função, em que: [EXIGÊNCIA DE CÓDIGO 6 de 8]; 
#Deve-se pergunta qual opção deseja (1. Cadastrar Livro / 2. Consultar Livro / 3. Remover Livro / 4. Encerrar Programa): 
#Se Cadastrar Livro, acrescentar em um id_ global e chamar a função cadastrar_livro(id_ global); 
#Se Consultar Livro, chamar função consultar_livro(); 
#Se Remover Livro, chamar função remover_livro(); 
#Se Encerrar Programa, sair do menu (e com isso acabar a execução do código); 
#Se Entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida" e repetir a pergunta F.a. 
#Enquanto o usuário não escolher a opção 4, o menu deve se repetir. 
#Deve-se implementar uma lista de dicionários (uma lista contento dicionários dentro) [EXIGÊNCIA DE CÓDIGO 7 de 8]; 
#Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 8 de 8]; 
#Deve-se apresentar na saída de console uma mensagem de boas-vindas com o seu nome [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 6]; 
#Deve-se apresentar na saída de console um cadastro de 3 livros (sendo 2 deles no mesmo autor) [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 6]; 
#Deve-se apresentar na saída de console uma consulta de todos os livros [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 6]; 
#Deve-se apresentar na saída de console uma consulta por código (id) de um dos livros [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 6]; 
#Deve-se apresentar na saída de console uma consulta por autor em que 2 livros sejam do mesmo autor [EXIGÊNCIA DE SAÍDA DE CONSOLE 5 de 6]; 
#Deve-se apresentar na saída de console uma remoção de um dos livros seguida de uma consulta de todos os livros [EXIGÊNCIA DE SAÍDA DE CONSOLE 6 de 6];

# Mensagem de boas-vindas
from enum import auto 
# print("Bem-vindo(a) ao sistema de livros, " + nome)
print("-" * 20, "Bem-vindo ao sistema de gerenciamento de livro!", "-" * 20)
print("-" * 44, "-" * 44) # Linha de separação
nome = "Lucas Matheus" # Nome do usuário
print(f"Olá, {nome}")  # Mensagem de boas-vindas com o nome do usuário

lista_livro = [] # Lista vazia para armazenar os livros
id_global = 0 # Variável para armazenar o id global

def cadastrar_livro(id): # Função para cadastrar um livro
    nome_livro = input("Digite o nome do livro: ") # Pergunta o nome do livro
    autor_livro = input("Digite o autor do livro: ") 
    editora_livro = input("Digite a editora do livro: ")

    livro = { # Dicionário para armazenar os dados do livro
        "ID": id,
        "Nome": nome_livro,
        "Autor": autor_livro,
        "Editora_livro": editora_livro
    }

    lista_livro.append(livro) # Adiciona o livro à lista
    print(f"\nLivro cadastrado com sucesso! ID: {id}\n") # Mensagem de confirmação

def consultar_livro(): # Função para consultar os livros
    while True: # Loop infinito para consultar livros
        print("\nConsultar Livro")
        print("1. Consultar Todos")
        print("2. Consultar por ID")
        print("3. Consultar por Autor")
        print("4. Retornar ao Menu")
        
        opcao = input("Escolha uma opção: ") 
        
        if opcao == "1": # Se a opção for 1, consultar todos os livros
            if lista_livro:
                print("\nLista de Livros:")
                for livro in lista_livro:
                    print(livro)
            else:
                print("\nNenhum livro cadastrado.")
 
        elif opcao == "2": # Se a opção for 2, consultar por ID
            try:
                id_consulta = int(input("\nDigite o ID do livro: "))
                encontrado = False
                for livro in lista_livro:
                    if livro["ID"] == id_consulta: # Se o ID for encontrado
                        print(livro)
                        encontrado = True
                        break
                if not encontrado: # Se o ID não for encontrado
                    print("\nID não encontrado.")
            except ValueError:
                print("\nID inválido. Digite um número.")

        elif opcao == "3": # Se a opção for 3, consultar por autor
            autor_consulta = input("\nDigite o nome do autor: ")
            encontrados = [livro for livro in lista_livro if livro["Autor"].lower() == autor_consulta.lower()]
            if encontrados:
                for livro in encontrados: # Se o autor for encontrado
                    print(livro)
            else:
                print("\nNenhum livro encontrado para esse autor.")

        elif opcao == "4": # Se a opção for 4, retornar ao menu
            break

        else:
            print("\nOpção inválida. Tente novamente.")

def remover_livro(): # Função para remover livros
    """Função para remover um livro pelo ID"""
    while True:
        try:
            id_remover = int(input("\nDigite o ID do livro a ser removido: "))
            for livro in lista_livro: # Percorrer a lista de livros
                if livro["ID"] == id_remover: # Se o ID for encontrado
                    lista_livro.remove(livro)
                    print("\nLivro removido com sucesso.")
                    return 
            print("\nID inválido. Tente novamente.")
        except ValueError: 
            print("\nID inválido. Digite um número.")

# Menu principal
while True: # Loop infinito para manter o programa rodando
    print("-" * 35, "Menu Principal", "-" * 38)
    print("1. Cadastrar Livro")
    print("2. Consultar Livro")
    print("3. Remover Livro")
    print("4. Encerrar Programa")
    
    escolha = input("Escolha uma opção: ") # Solicitar a escolha do usuário

    if escolha == "1": # Se a escolha for 1, cadastrar livro
        id_global += 1
        cadastrar_livro(id_global)

    elif escolha == "2": # Se a escolha for 2, consultar livro
        consultar_livro()

    elif escolha == "3": # Se a escolha for 3, remover livro
        remover_livro()

    elif escolha == "4": 
        print("\nEncerrando o programa...")
        break

    else:
        print("\nOpção inválida. Tente novamente.")

