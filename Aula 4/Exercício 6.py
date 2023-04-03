horas_trab = input("Quantas horas você trabalhou no mês")
valor_hora = input("Quanto vale a sua hora trabalhada?")
desconto = input("Qual o seu percentual de desconto?")

valor = int(valor_hora)
horas = int(horas_trab)
percentual = int(desconto)
salario = horas * valor
desconto = (percentual * salario)/100
liquido = salario - desconto

print ("Seu salario bruto é de :", salario)
print ("O total descontado do seu salário é de :", desconto)
print ("O seu salario liquido é de : ", liquido)
