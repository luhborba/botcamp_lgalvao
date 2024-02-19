# Recebendo os valores de Entrada
nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: "))
bonus = float(input("Digite o valor do bônus: "))

# Regra do Bonus é : 1000 + salario * bônus

# Definindo Constante do valor do bônus
CONSTANTE_BONUS = 1000

# Calculando Valor do Bônus
valor_bonus = CONSTANTE_BONUS + salario * bonus

# Mostrando o resultado
print(f"O usuário {nome} tem um bônus de R${valor_bonus:.2f}")
