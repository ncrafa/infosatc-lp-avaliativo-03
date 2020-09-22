
senha=[]
apto=[]
cpf=[]
nome=[]
usuario=0
for x in range(5):
    descricao=""
    escolha=""
    conta=0
    print("")
    idade=(int(input("Insira a sua idade: ")))
    peso=(float(input("Insira o seu peso: ")))
    tempo=(float(input("Insira quantas horas de sono tiveste na ultima noite: ")))
    if idade>16 and idade<69:
        conta+=1
    else:
        descricao="idade "+descricao
    if peso>50:
        conta+=1
    else:
        descricao="peso "+descricao
    if tempo>6:
        conta+=1
    else:
        descricao="sono "+descricao
    if conta==3:
        print("Pode doar sangue")
        escolha=(input("Deseja se cadastrar?(s/n): "))
        if(escolha=="s"):
            usuario=usuario+1
            variavel=(input("Insira seu nome: "))
            nome.append(variavel)
            variavel=(float(input("Insira seu cpf: ")))
            cpf.append(variavel)
            variavel=(input("Insira sua senha: "))
            senha.append(variavel)
            variavel=(input("Está apto a doar? "))
            apto.append(variavel)
        else:
            pass
    else:
        print("Não pode doar sangue pois não atingiu o experado nas categorias de:",descricao)

for x in range(usuario):
    print("")
    print("O nome do usuario ",x," é ",nome[x])
    print("O cpf do usuario ",x," é ",cpf[x])
    print("A senha do usuario ",x," é ",senha[x])
    print("O usuario ",x," esta apto? ",apto[x])