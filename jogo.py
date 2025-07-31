import random
print("#######################")
print("# jogo de adivinhação #")
print("#  Welliton h.        #")
print("#                     #")
print("#  #    #     #       #")
print("#  #   # #    #       #")
print("#   # #   #  #        #")
print("#    #     #          #")
print("#                     #")
print("#  #       #          #")
print("#  #       #          #")
print("#  # # # # #          #")
print("#  #       #          #")
print("#  #       #          #")
print("# ------------------- #")
print("#  #                  #")
print("#  #     ###########  #")
print("#  #                  #")
print("#  #                  #")
print("#        ###########  #")
print("#  #                  #")
print("#                     #")
print("#######################")
numeroSecreto = random.randrange(0,100)
totaltentativas = 0
pontos = 100

print("Qual o níveis de dificuldade?")
print("1-(fácil)-2-(médio)-3-difícil")
nivel = int(input("Escolha um nível: "))
if nivel == 1:
    print ("você é um mariquinha! (FÁCIL)")
    print ("Agora você tem 20 tentativas!")
    totaltentativas = 20
elif nivel == 2:
    print("você não especial (MÉDIO)")
    print ("Agora você tem 10 tentativas!")
    totaltentativas = 10
else:
    print("você é burro? (DÍFICIL)")
    print ("Agora você tem 5 tentativas!")
    totaltentativas = 5