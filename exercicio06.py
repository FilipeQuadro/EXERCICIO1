peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")