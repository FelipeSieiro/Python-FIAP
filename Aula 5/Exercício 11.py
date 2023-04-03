j1 = int(input('J1 Quantos blocos você empilhou?: '))
j2 = int(input('J2 Quantos blocos você empilhou?: '))
j3 = int(input('J3 Quantos blocos você empilhou?: '))

mais_blocos_empilhados = j1

if (j2 > mais_blocos_empilhados):
    mais_blocos_empilhados = j2
if (j3 > mais_blocos_empilhados):
    mais_blocos_empilhados = j3

print('O jogador que ganhou, empilhou:',mais_blocos_empilhados, "Blocos")