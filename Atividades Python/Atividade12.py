n1 = float(input("Digite a Primeira Nota: "))
n2 = float(input("Digeta a Segunda Nota: "))
n3 = float(input("Digite a Terceira Nota: "))
media_e = float(input("Media dos exercicios:"))

media_a =  float(n1 + n2 * 2 + n3 * 3 + media_e) / 7

if media_a >=90:
	print("Aprovado, A", media_a)
	
elif media_a >= 75 and media_a < 90:
	print("Aprovado, B", media_a)

elif media_a >= 60 and media_a < 75:
	print("Aprovado, C", media_a)

elif media_a >= 40 and media_a < 60:
	print("Reprovado, D" , media_a)

else:
	print("Reprovado, E" , media_a)