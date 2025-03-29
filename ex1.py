# QUESTÃO 1 de 4 – Conteúdos até Aula 3 

#Enunciado: Imagina-se que você é um dos programadores responsáveis pela 
# construção de um app de vendas para uma determinada empresa X que vende em atacado. 
# Uma das estratégias de vendas dessa empresa X é dar desconto maior conforme o valor da compra, 
# conforme a listagem abaixo: 
#Se valor for menor que 2500 o desconto será de 0%; 
#Se valor for igual ou maior que 2500 e menor que 6000 o desconto será de 4%; 
#Se valor for igual ou maior que 6000 e menor que 10000 o desconto será de 7%; 
#Se valor for igual ou maior que 10000 o desconto será de 11%;

#Elabore um programa em Python que: 
#Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome e sobrenome [EXIGÊNCIA DE CÓDIGO 1 de 6]; 
#Deve-se implementar o input do valor unitário e da quantidade do produto [EXIGÊNCIA DE CÓDIGO 2 de 6]; 
#Deve-se implementar o desconto conforme a enunciado acima (obs.: atente-se as condições de menor, igual e maior) [EXIGÊNCIA DE CÓDIGO 3 de 6]; 
#Deve-se implementar o valor total sem desconto e o valor total com desconto [EXIGÊNCIA DE CÓDIGO 4 de 6]; 
#Deve-se implementar as estruturas if, elif e else (todas elas) [EXIGÊNCIA DE CÓDIGO 5 de 6];   
#Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 6 de 6]; 
#Deve-se apresentar na saída de console uma mensagem de boas-vindas com seu nome [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 2]; 
#Deve-se apresentar na saída de console um pedido recebendo desconto (valor total sem desconto maior ou igual a 2500) [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 2]; 

# Saudação ao usuário
saudacao = "Bem-vindo"
nome = "Lucas Matheus"

# Exibe a saudação
print(f"{saudacao}, {nome}")
# Entrada de valores
valor_unitario = float(input("Informe o valor Unitário do item: "))  # Aceita valores decimais
quantidade = int(input("Digite agora a quantidade: "))
# Cálculo do valor total sem desconto
valor_total = valor_unitario * quantidade
# Aplicação do desconto conforme as condições
if valor_total < 2500:
    desconto = 0
elif valor_total >= 2500 and valor_total < 6000:
    desconto = valor_total * 0.04  # 4% de desconto
elif valor_total >= 6000 and valor_total < 10000:
    desconto = valor_total * 0.07  # 7% de desconto
elif valor_total >= 10000:
    desconto = valor_total * 0.11  # 11% de desconto
else:
    print("Valor inválido")
    desconto = 0  # Caso de erro, mas não é necessário
# Cálculo do valor total com desconto
valor_com_desconto = valor_total - desconto
# Exibição dos valores formatados
print(f"\nValor total sem desconto: R$ {valor_total:.2f}")
print(f"Valor total com desconto: R$ {valor_com_desconto:.2f}")
