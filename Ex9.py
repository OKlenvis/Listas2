Funcionarios=[]
add=input("Deseja adicionar um funcionario? (S/N): ")
while add == "S" or add == "s":
    id=input("Digite o ID do funcionario: ")
    nome=input("Digite o nome do funcionario: ")
    cargo=input("Digite o cargo do funcionario: ")
    salario=input("Digite o salario do funcionario: ")
    add=[id, nome, cargo, salario]
    Funcionarios.append(add)
    print(f"\n{Funcionarios}\n")
    add=input("Deseja adicionar outro funcionario? (S/N): ")
    if add == "N" or add == "n":
        print(f"\n{Funcionarios}\n")
        print("Obrigado por utilizar o sistema!")
        break