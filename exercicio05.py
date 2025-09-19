preco = float(input("Digite o preço do produto: "))

desconto = preco * 0.10
preco_final = preco - desconto

print(f"O preço final com desconto é: R$ {preco_final:.2f}")