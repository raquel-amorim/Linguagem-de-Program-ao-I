def beber(idade):

    if idade>=18:
        print("Pode beber! ")

    elif idade<18 and idade>0:
        acomp = str(input("Você está acompanhado de algum responsável? "))
        if acomp == "sim":
            print("Pode beber se seu responsável deixar, mas faz isso escondido tá?")
        else:
            print("Não pode beber!")
    
    else:
        print("Insira uma idade válida!")

idade = int(input("Qual sua idade? "))
beber(idade)
