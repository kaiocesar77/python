while True:
	valor = float(input("Digite o valor do produto: "))

	print("Opções de pagamento:")
	print("1. À vista em dinheiro ou cheque, recebe 10% de desconto")
	print("2. À vista no cartão de crédito, recebe 15% de desconto")
	print("3. Em duas vezes, preço normal de etiqueta sem juros")
	print("4. Em duas vezes, preço normal de etiqueta mais juros de 10%")

	forma_pagar = int(input("Digite o número equivalente a sua forma de pagamento:"))

	if forma_pagar == 1:
		print("Seu produto com desconto ficou:" ,"R$",round((valor/100) * valor - 10, 1))
  
	elif forma_pagar == 2:  
		print("Seu produto com desconto ficou:" ,"R$",round((valor/100) * valor - 15, 1))

	elif forma_pagar == 3:
		print("Terá que pagar em duas parcelas de:" ,"R$",round(valor / 2, 1))

	elif forma_pagar == 4:
		print("Terá que pagar em duas parcelas de:","R$", round((valor/2)+5,1))

	else:
		print("Escolha uma opção de pagamento valida")