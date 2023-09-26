nome = input("Qual seu nome?")
print("Prazer em te conhecer", nome)

renda = float(input("Digite seu salário:"))
 
if renda <= 2112.00:
	print("Você não precisa pagar o Imposto de renda", renda)
    
elif renda <= 2826.65:
	taxa = renda - (renda * 0.075)
	print("Você pagou uma taxa de 7,5%. Agora seu salário é de:", round(taxa, 2))
    
elif renda <= 3751.05:
	taxa = renda - (renda * 0.15)
	print("Você pagou uma taxa de 15%. Agora seu salário é de:", round(taxa, 2))

elif renda <= 4664.68:
	taxa = renda - (renda * 0.225)
	print("Você pagou uma taxa de 22,5%. Agora seu salário é de:", round(taxa, 2))

else:
	taxa = renda - (renda * 0.275)
	print("Você pagou uma taxa de 27,5%. Agora seu salário é de:", round(taxa, 2))