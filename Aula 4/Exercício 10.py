print("Conselheiro 21:)")

carta1 = input(" Digite o valor da primeira carta :")
carta2 = input(" Digite o valor da segunda carta :")

c1 = int(carta1)
c2 = int(carta2)

soma = c1 + c2

if soma<=10:
    print("Sem dúvida compre mais uma carta")
elif soma>10 and soma<=15:
    print("Há um risco, mas aconselho a comprar mais uma carta")
elif soma>15 and soma<=20:
    print("Aconselho a parar de jogar")
elif soma==21:
    print("Você já venceu, não precisa comprar mais nada")
else:
    print("Você perdeu o jogo")
