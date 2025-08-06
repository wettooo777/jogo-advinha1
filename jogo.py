import random

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'

print(f"{RED}#######################{RESET}")
print(f"{RED}#{RESET} {MAGENTA}jogo de adivinhação{RESET} {RED} #{RESET}")
print(f"{RED}#{RESET} {BLUE}    Welliton h.    {RESET} {RED}#{RESET}")
print(f"{RED}#######################{RESET}")
print(f"{YELLOW}")


numeroSecreto = random.randrange(0,100)
totaltentativas = 0
pontos = 1000

print(f"{YELLOW}Qual o níveis de dificuldade?{RESET}")
print(f"1-{BLUE}(fácil){RESET}-2-{YELLOW}(médio){RESET}-3-{RED}(difícil){RESET}-4-{MAGENTA}(treino){RESET}")
nivel = int(input(f"Escolha um nível: "))

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
    print("Nesse modo não terá nenhum desafio")
    print(f"Número secreto: {numeroSecreto}")

else:
    print(f"{RED}Essa dificuldade não existe{RED}")

for rodada in range (1, totaltentativas +1):

    barra = "#" * rodada
    print (f"{MAGENTA} {[barra]} {RESET} ({rodada}/{totaltentativas}) {BLUE}Tentativas usadas{RESET}")
    chute_str = input("Digite um número entre 1 e 100: ")

    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print(f"{RED}Número invalido{RESET}")
        continue
    
    acertou = chute == numeroSecreto
    maior = chute > numeroSecreto
    menor = chute < numeroSecreto

    if (acertou):
        print(f"{GREEN}Você acertou e fez {pontos}{RESET}! ")
        break

    else:
        if(maior):
            print(f"{RED}Você errou!Seu chute foi maior que número secreto{RESET}")
        elif(menor):
            print(f"{RED}Você errou! Seu chute foi menor que número secreto{RESET}")

            pontosperdidos = abs(numeroSecreto - chute)
            pontos = pontos - pontosperdidos

print (f"{CYAN}Fim de jogo! O número era: {RESET}",numeroSecreto)
