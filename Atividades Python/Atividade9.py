sexo = str(input("Digite seu Sexo(masculino/feminino): "))
altura = float(input("Digite sua altura: "))

if sexo == "masculino" or sexo == "Masculino":
    calculo1 = (72.7 * altura) - 58
    print("Seu peso ideal é: " , round(calculo1 , 1))
elif sexo == "feminino" or sexo == "Feminino":
    calculo2 = (62.1 * altura) - 44.7
    print("Seu peso ideal é" , round(calculo2 , 1))    