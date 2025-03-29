#QUESTÃO 2 de 4 - Conteúdo até aula 04 

#Enunciado: Você e sua equipe de programadores foram contratados para 
# desenvolver um app de vendas para uma loja que vende Açaí e Cupuaçu. 
# Você ficou com a parte de desenvolver a interface do cliente para retirada do produto. 

#A Loja possui seguinte relação: 
#Tamanho P de Cupuaçu (CP) custa 9 reais e o Açaí (AC) custa 11 reais; 
#Tamanho M de Cupuaçu (CP) custa 14 reais e o Açaí (AC) custa 16 reais; 
#Tamanho G de Cupuaçu (CP) custa 18 reais e o Açaí (AC) custa 20 reais; 

#Elabore um programa em Python que:  
#Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome e sobrenome [EXIGÊNCIA DE CÓDIGO 1 de 8]; 
#Deve-se implementar o input do sabor (CP/AC) e o print “Sabor inválido. Tente novamente" se o usuário entra com valor diferente de CP e AC [EXIGÊNCIA DE CÓDIGO 2 de 8]; 
#Deve-se implementar o input do tamanho (P/M/G) e o print “Tamanho inválido. Tente novamente" se o usuário com entra valor diferente de P, M ou G [EXIGÊNCIA DE CÓDIGO 3 de 8]; 
#Deve-se implementar if, elif e/ou else, utilizando o modelo aninhado (aula 3 – Tema 4) com cada uma das combinações de sabor e tamanho [EXIGÊNCIA DE CÓDIGO 4 de 8]; 
#Deve-se implementar um acumulador para somar os valores dos pedidos [EXIGÊNCIA DE CÓDIGO 5 de 8]; 
#Deve-se implementar o input com a pergunta: “Deseja pedir mais alguma coisa?”. Se sim repetir a partir do item B, senão encerrar o programa executar o print do acumulador [EXIGÊNCIA DE CÓDIGO 6 de 8]; 
#Deve-se implementar as estruturas de while, break, continue (todas elas) [EXIGÊNCIA DE CÓDIGO 7 de 8]; 
#Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 8 de 8]; 
#Deve-se apresentar na saída de console uma mensagem de boas-vindas com o seu nome [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4]; 
#Deve-se apresentar na saída de console um pedido em que o usuário errou o sabor [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4];  
#Deve-se apresentar na saída de console um pedido em que o usuário errou o tamanho [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4]; 
#Deve-se apresentar na saída de console um pedido com duas opções sabores diferentes e com tamanhos diferentes [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4];

# Saudação ao usuário
# Mensagem de boas-vindas
print("Bem-vindo (a) ao nosso app de vendas de Açaí e Cupuaçu!")
print("-" * 20 + "Cardápio" + "-" * 20, "\n") 
print("-" * 48, "\n")
print("-------| Tamanho | Cupuaçu | Açaí |-------")
print("-------| P       | 9       | 11   |-------")
print("-------| M       | 14      | 16   |-------")
print("-------| G       | 18      | 20   |-------")
nome = "Lucas Matheus, posso ajudar?"
print(f"Olá, {nome}")

# Dicionário com os preços
tabela_precos = {
    "CP": {"P": 9, "M": 14, "G": 18},
    "AC": {"P": 11, "M": 16, "G": 20}
}

# Inicializa a variável para o total do pedido
total_pedido = 0  

while True:
    # Solicita o sabor
    sabor = input("Informe o sabor (CP para Cupuaçu / AC para Açaí): ").strip().upper()
    
    if sabor not in tabela_precos:
        print("Sabor inválido. Tente novamente.")
        continue  # Retorna para o início do loop

    # Solicita o tamanho
    tamanho = input("Informe o tamanho (P / M / G): ").strip().upper()

    if tamanho not in tabela_precos[sabor]:  
        print("Tamanho inválido. Tente novamente.")
        continue  # Retorna para o início do loop

    # Obtém o preço e soma ao total
    preco = tabela_precos[sabor][tamanho]
    total_pedido += preco
    print(f"Item adicionado: {sabor} {tamanho} - R$ {preco}")

    # Pergunta se deseja adicionar mais itens
    mais_pedido = input("Deseja pedir mais alguma coisa? (S/N): ").strip().upper()
    if mais_pedido != "S":
        break  # Sai do loop se a resposta não for "S"

# Exibe o valor total do pedido
print(f"Total do pedido: R$ {total_pedido:.2f}")

