print("Sistema de Gestão de bicicletas")

print("(L)ogin")
print("(C)adstrar Bicicleta")
print("(S)air")

opcao = input("Por favor Digite Sua Opção: ")

print("Você escolheu a opção:", opcao).upper()

    while (opcao != "S"):
        if opcao == "L":
            print("Tela de Login")
            user = input("User: ")
            senha = input("Senha: ")
        else:
            if  opcao == "C":
                print ("Tela de Cadastro")
                modelo = input("Digite o modelo da sua Bike: ")
            else: 
                print("Saindo do Sistema")
