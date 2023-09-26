peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / altura ** 2

if imc <= 18.5:
    print("Você está abaixo do peso", round(imc,1))
elif imc <= 25:
    print("Você está no peso ideal", round(imc,1))
elif imc <= 30:
    print("Você está acima do peso", round(imc,1)) 
else:
    print("Você está Obeso", round(imc,1))    