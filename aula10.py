# ***Desafio 1 Condicionais***

# ***Crie um sistema de e-commerce, onde o usuário possa:***

# ***cadastrar-se***
# ***comprar um produto***
# ***descobrir o valor total***
# **pagar***

# Produtos

produtos = ["smartphone", "TV", "microondas", "batedeira"]
precos = [1300.00, 1000.00, 250.00, 170.00]

carrinho = []
total = 0

nome = input("Digite seu nome: ")
tel = int(input("Digite seu telefone: "))
print(f"Cadastro realizado! Bem-vindo, {nome}")

print(f"Temos alguns produtos disponíveis: {produtos}")

escolha1 = input("Escolha um produto pelo número (ou '0' para finalizar): ")

if escolha1 == '1':
    carrinho.append(produtos[0])
    total += precos[0]
    
elif escolha1 == '2':
    carrinho.append(produtos[1])
    total += precos[1]
   
elif escolha1 == '3':
    carrinho.append(produtos[2])
    total += precos[2]
    
elif escolha1 == '4':
    carrinho.append(produtos[3])
    total += precos[3]

elif escolha1 == '5':
    carrinho.append(produtos[4])
    total += precos[4]

escolha2 = input("Escolha um produto pelo número (ou '0' para finalizar): ")

if escolha2 == '1':
    carrinho.append(produtos[0])
    total += precos[0]
    
elif escolha2 == '2':
    carrinho.append(produtos[1])
    total += precos[1]
    
elif escolha2 == '3':
    carrinho.append(produtos[2])
    total += precos[2]
    
elif escolha2 == '4':
    carrinho.append(produtos[3])
    total += precos[3]
    
elif escolha2 == '5':
    carrinho.append(produtos[4])
    total += precos[4]



escolha3 = input("Escolha um produto pelo número (ou '0' para finalizar): ")

if escolha3 == '1':
    carrinho.append(produtos[0])
    total += precos[0]
    
elif escolha3 == '2':
    carrinho.append(produtos[1])
    total += precos[1]
    
elif escolha3 == '3':
    carrinho.append(produtos[2])
    total += precos[2]
    
elif escolha3 == '4':
    carrinho.append(produtos[3])
    total += precos[3]
    
elif escolha3 == '5':
    carrinho.append(produtos[4])
    total += precos[4]


escolha4 = input("Escolha um produto pelo número (ou '0' para finalizar): ")

if escolha4 == '1':
    carrinho.append(produtos[0])
    total += precos[0]
    
elif escolha4 == '2':
    carrinho.append(produtos[1])
    total += precos[1]
    
elif escolha4 == '3':
    carrinho.append(produtos[2])
    total += precos[2]
    
elif escolha4 == '4':
    carrinho.append(produtos[3])
    total += precos[3]
    
elif escolha4 == '5':
    carrinho.append(produtos[4])
    total += precos[4]
   

    print("\nVocê comprou:")
if len(carrinho) > 0:
    print(carrinho)
    print(f"Total: R$ {total:.2f}")
else:
    print("Nenhum produto comprado.")