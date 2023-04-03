lrg_triangulo= int(input("Qual a largura do triangulo?: "))
lrg_atual = 1


while lrg_triangulo > lrg_atual:
      print("*" * lrg_atual)
      lrg_atual += 1
else:
      while lrg_atual > 0:
        print("*" * lrg_atual)
        lrg_atual -= 1