print(" Programa que calcula as Notas")
notas = []


for i in range(6):
    cp1 = float(input("Digite a nota do" +" " + "CHECKPOINT #{}:  ".format(i+1)))
    notas.append(cp1)

ch1 = float(input("Digite a nota do Challenge 1: "))
notas.append(ch1)

ch2 = float(input("Digite a nota do Challenge 2: "))
notas.append(ch2)

gs = float(input("Digite a nota da Global Solution: "))
notas.append(gs)


print("Suas notas são: ")
print(notas)

soma = 0
for n in notas:
    soma = soma + n
media = soma / 9.0
print("Sua média é: ")
print(media)