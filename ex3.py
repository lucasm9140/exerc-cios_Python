#QUESTÃO 3 de 4 - Conteúdo até aula 05 

#Enunciado: Você foi contratado para desenvolver um sistema de cobrança de serviços de uma copiadora. Você ficou com a parte de desenvolver a interface com o funcionário.
#A copiadora opera da seguinte maneira: 
#Serviço de Digitalização (DIG) o custo por página é de um real e dez centavos; 
#Serviço de Impressão Colorida (ICO) o custo por página é de um real;  
#Serviço de Impressão Preto e Branco (IPB) o custo por página é de quarenta centavos;  
#Serviço de Fotocópia (FOT) o custo por página é de vinte centavos;  
#Se número de páginas for menor que 20 retornar o número de página sem desconto; 
#Se número de páginas for igual ou maior que 20 e menor que 200 retornar o número de páginas com o desconto é de 15%; 
#Se número de páginas for igual ou maior que 200 e menor que 2000 retornar o número de páginas com o desconto é de 20%; 
#Se número de páginas for igual ou maior que 2000 e menor que 20000 retornar o número de páginas com o desconto é de 25%; 
#Se número de páginas for maior ou igual à 20000 não é aceito pedidos nessa quantidade de páginas; 
#Para o adicional de encadernação simples (1) é cobrado um valor extra de 15 reais; 
#Para o adicional de encadernação de capa dura (2) é cobrado um valor extra de 40 reais; 
#Para o adicional de não querer mais nada (0) é cobrado um valor extra de 0 reais; 
#O valor final da conta é calculado da seguinte maneira: 
#total = (servico * num_pagina) + extra 

#Elabore um programa em Python que:  
#Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome [EXIGÊNCIA DE CÓDIGO 1 de 7]; 
#Deve-se implementar a função escolha_servico() em que: [EXIGÊNCIA DE CÓDIGO 2 de 7]; 
#Pergunta o servico desejado; 
#Retorna o valor servico com base na escolha do usuário; 
#Repete a pergunta do item B.a se digitar uma opção diferente de: dig/ico/ipb/fot; 
#Deve-se implementar a função num_pagina() em que: [EXIGÊNCIA DE CÓDIGO 3 de 7]; 
#Pergunta o número de páginas; 
#Retorna o número de páginas com desconto seguindo a regra do enunciado (desconto calculado em cima do número de páginas); 
#Repete a pergunta do item C.a se digitar um valor acima de 20000 ou valor não numérico (use try/except para não numérico) 
#Deve-se implementar a função servico_extra() em que: [EXIGÊNCIA DE CÓDIGO 4 de 7]; 
#Pergunta pelo serviço adicional; 
#Retornar o valor de apenas uma das opções de adicional  
#Repetir a pergunta item D.a se digitar uma opção diferente de: 1/2/0; 
#Deve-se implementar o total a pagar no código principal (main), ou seja, não pode estar dentro de função, conforme o enunciado [EXIGÊNCIA DE CÓDIGO 5 de 7]; 
#Deve-se implementar try/except [EXIGÊNCIA DE CÓDIGO 6 de 7]; 
#Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 7 de 7]; 
#Deve-se apresentar na saída de console uma mensagem de boas-vindas com o seu nome [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4]; 
#Deve-se apresentar na saída de console um pedido no qual o usuário errou a opção de serviço [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4]; 
#Deve-se apresentar na saída de console um pedido no qual o usuário digitou ultrapassou no número de páginas [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4]; 
#Deve-se apresentar na saída de console um pedido com opção de serviço, número de páginas e serviço extra válidos [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4];

# Mensagem de boas-vindas
print("Bem-vindo ao sistema de cobrança da copiadora!")
nome = "Lucas Matheus"
print(f"Olá, {nome}")

# Dicionário com os preços dos serviços
servicos = {
    "DIG": 1.10,  # Digitalização
    "ICO": 1.00,  # Impressão Colorida
    "IPB": 0.40,  # Impressão Preto e Branco
    "FOT": 0.20   # Fotocópia
}

def escolha_servico(): # Função para escolher o serviço
    """Solicita e valida a escolha do serviço."""
    while True: # Loop para repetir a pergunta caso o usuário digite uma opção inválida
        servico = input("Escolha o serviço (DIG/ICO/IPB/FOT): ").strip().upper() # Solicita a escolha do serviço
        if servico in servicos: # Verifica se a opção escolhida está no dicionário
            return servicos[servico] # Retorna o preço do serviço escolhido
        else: # Caso a opção escolhida não esteja no dicionário
            print("Serviço inválido. Tente novamente.") # Exibe uma mensagem de erro

def num_pagina(): # Função para escolher o número de páginas
    """Solicita e valida o número de páginas, aplicando descontos.""" 
    while True: # Loop para repetir a pergunta caso o usuário digite um valor inválido
        try: # Tenta executar o bloco de código
            paginas = int(input("Informe o número de páginas: ")) # Solicita o número de páginas
            if paginas >= 20000: # Verifica se o número de páginas ultrapassou a quantidade máxima
                print("Quantidade de páginas não permitida. Tente novamente.")
                continue # Pula para a próxima iteração do loop
            # Aplicação de descontos
            if paginas < 20: # Se o número de páginas for menor que 20
                return paginas * 1.00 # Retorna o valor sem desconto
            elif paginas < 200:
                return paginas * 0.85
            elif paginas < 2000:
                return paginas * 0.80
            elif paginas < 20000: # Se o número de páginas for menor que 20.000
                return paginas * 0.75 # Retorna o valor com desconto de 25%
        except ValueError: # Caso o usuário digite um valor inválido
            print("Entrada inválida. Digite um número inteiro válido.")

def servico_extra(): # Função para escolher o serviço extra
    """Solicita e valida a escolha do serviço adicional."""
    adicionais = {"1": 15.00, "2": 40.00, "0": 0.00} # Dicionário com os preços dos serviços adicionais
    while True: # Loop para repetir a pergunta caso o usuário digite uma opção inválida
        extra = input("Escolha o serviço extra (1 - Encadernação simples, 2 - Capa dura, 0 - Nenhum): ").strip()
        if extra in adicionais: # Verifica se a opção escolhida está no dicionário
            return adicionais[extra] # Retorna o preço do serviço extra escolhido
        else:
            print("Opção inválida. Tente novamente.") # Exibe uma mensagem de erro

# Código principal (main) da aplicação
valor_servico = escolha_servico() # Chama a função para escolher o serviço
n_paginas = num_pagina() # Chama a função para escolher o número de páginas
valor_extra = servico_extra() # Chama a função para escolher o serviço extra

total = (valor_servico * n_paginas) + valor_extra # Calcula o valor total da impressão

print(f"Total a pagar: R$ {total:.2f}")  # Exibe o valor total da impressão com duas casas decimais