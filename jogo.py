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
elif nivel == 3:
    print("você é burro? (DÍFICIL)")
    print ("Agora você tem 5 tentativas!")
    totaltentativas = 5
else:
    print("Essa dificuldade não existe")
for rodada in range (1, totaltentativas +1):
    print ("Tentativas {} de {}".format(rodada, totaltentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Número invalido")
        continue
    
    acertou = chute == numeroSecreto
    maior = chute > numeroSecreto
    menor = chute < numeroSecreto

    if (acertou):
        print(f"Você acertou e fez {pontos}! ")
        break
    else:
        if(maior):
            print("Você errou!Seu chute foi maior que número secreto")
        elif(menor):
            print("Você errou! Seu chute foi menor que número secreto")

            pontosperdidos = abs(numeroSecreto - chute)
            pontos = pontos - pontosperdidos

print("Fim de jogo! O número era ",numeroSecreto)
