import random

print("#######################")
print("# jogo de adivinhação #")
print("#     Welliton h.     #")
print("#######################")

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'

numeroSecreto = random.randrange(0,100)
totaltentativas = 0
pontos = 1000

print(f"{YELLOW}Qual o níveis de dificuldade?{RESET}")
print("1-(fácil)-2-(médio)-3-(difícil)-4-(treino)")
nivel = int(input("Escolha um nível: "))

if nivel == 1:
    print (f"{BLUE}você deve estar brincando! (FÁCIL){RESET}")
    print ("Agora você tem 20 tentativas!")
    totaltentativas = 20

elif nivel == 2:
    print(f"{GREEN}Boa sorte! (MÉDIO){RESET}")
    print ("Agora você tem 10 tentativas!")
    totaltentativas = 10

elif nivel == 3:
    print(f"{RED}você é tem certeza? (DÍFICIL){RESET}")
    print ("Agora você tem 5 tentativas!")
    totaltentativas = 5

elif nivel == 4:
    print(f"{MAGENTA}Porque? (TREINO)")
    print("Nesse modo ele não terá nenhum desafio")
    print(f"Número secreto: {numeroSecreto}")

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
