idadeHomem=0
homem=0
idadeMulher=0
mulher=0

for x in range(10):
    sexo=(input("Insira o seu sexo (m/f): "))
    if sexo=="m":
         mulher=mulher+1
         idadeMulher=idadeMulher+(int(input("Informe sua idade: ")))
    else:
        homem=homem+1
        idadeHomem=idadeHomem+(int(input("Informe sua idade: ")))



print("A media da idade dos homens é",idadeHomem/homem)
print("A media da idade das mulheres é",idadeMulher/mulher)
print("A Idade média do grupo",(idadeMulher+idadeHomem)/(homem+mulher))







