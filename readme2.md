Jogo de Adivinhação em Python
🎯 Objetivos Gerais
Introduzir conceitos básicos de programação Python
Desenvolver um projeto prático e interativo
Trabalhar com estruturas de controle, entrada/saída e bibliotecas
📚 Estrutura das Aulas
Aula 1: Introdução e Configuração Inicial
Objetivos:

Apresentar a estrutura básica de um programa Python
Introduzir o conceito de números aleatórios
Configurar as variáveis iniciais do jogo
Conteúdo:

# Aula 1 - Código Base
import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 0
pontos = 1000
Atividade Prática:

Modificar a mensagem de boas-vindas

Alterar o intervalo de números secretos

Testar diferentes valores iniciais de pontos

Aula 2: Níveis de Dificuldade e Estruturas Condicionais
Objetivos:

Implementar sistema de níveis de dificuldade

Trabalhar com estruturas condicionais (if/elif/else)

Entender conversão de tipos (input)

Conteúdo:

# Aula 2 - Níveis de Dificuldade
print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5
Atividade Prática:

Adicionar um novo nível de dificuldade

Implementar verificação para entrada inválida

Criar um sistema de dicas baseado no nível

Aula 3: Loop Principal e Lógica do Jogo
Objetivos:

Implementar o loop principal do jogo

Validar entrada do usuário

Desenvolver a lógica de comparação

Conteúdo:

# Aula 3 - Loop do Jogo
for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou ",chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Número inválido! Tente novamente.")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
Atividade Prática:

Modificar as mensagens de feedback

Implementar contador de tentativas restantes

Adicionar verificação para entrada não numérica

Aula 4: Sistema de Pontuação e Finalização
Objetivos:

Implementar sistema de pontuação dinâmica

Trabalhar com operações matemáticas

Finalizar o jogo com feedback adequado

Conteúdo:

# Aula 4 - Finalização
    if(acertou):
        print(f"Você acertou e fez {pontos} pontos!")
        break
    else:
        if(maior):
            print("Você errou! Seu chute foi maior que o número secreto.")
        elif(menor):
            print("Você errou! Seu chute foi menor que o número secreto.")
        
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print("Fim do jogo! O número era", numero_secreto)
Atividade Prática:

Modificar o cálculo de pontos perdidos

Implementar sistema de recorde

Adicionar opção para jogar novamente

🔍 Avaliação
Participação nas atividades práticas

Implementação de pelo menos uma melhoria no código

Compreensão dos conceitos através de questionário rápido

🧩 Desafios Extras Nível Iniciante
🔢 Desafios de Dificuldade Progressiva
Nível 1 - Modificações Simples:

Mensagens Personalizadas

Altere as mensagens do jogo para deixá-las mais divertidas
Ex: "ERROU! Tá frio..." (para chutes muito longe) ou "Quase! Esquentando..." (para chutes próximos)
Contador Visual

Mostre uma barra visual de tentativas: [####-----] (5/10 tentativas usadas)
Modo Treino

Adicione uma opção que mostre o número secreto (útil para testar o jogo)
Nível 2 - Lógica Básica: 4. Dica Par/Ímpar
python if numero_secreto % 2 == 0: print("Dica: O número é par!") else: print("Dica: O número é ímpar!") 

Palpite Anterior

Mostre o chute anterior para ajudar na estratégia
Faixa Numérica

Mostre automaticamente se o número está entre 1-50 ou 51-100 após 3 erros
Nível 3 - Melhorias Interativas: 7. Pontuação Colorida
- Use códigos ANSI para cores (simples):
python print("\033[32m"+str(pontos)+"\033[0m") # Verde para acerto 

Animação Simples

Adicione um "loading" fictício:
import time
print("Processando", end="")
for _ in range(3):
    time.sleep(0.5)
    print(".", end="")
print()
Histórico de Chutes

Armazene os chutes em uma lista e mostre ao final
🛠️ Desafios Técnicos Controlados
Validação de Input

Evite erros quando o usuário digitar texto:
try:
    chute = int(input("Digite um número: "))
except ValueError:
    print("Digite apenas números!")
Dica Progressiva

A cada 5 tentativas erradas, mostre a dezena do número:
if rodada % 5 == 0:
    print(f"Dica: O número está entre {numero_secreto//10*10} e {numero_secreto//10*10+10}")
Modo Infinito

Opção para continuar jogando até acertar (sem limite de tentativas)
🎮 Desafios Criativos
Tema Personalizado

Transforme o jogo em "Adivinhe o Pokémon" (usando números como IDs)
Sistema de Estrelas

Dê 1-5 estrelas baseado no desempenho:
estrelas = min(5, max(1, 5 - (rodada//(total_de_tentativas//5))))
print("★"*estrelas)
Versão Matemática

Substitua o número por uma equação simples (ex: "? = 5×3+2")
📊 Desafio Final Integrador
Relatório Simplificado
Ao final, mostre:
print(f"""
RELATÓRIO:
Tentativas: {rodada}/{total_de_tentativas}
Chutes: {', '.join(map(str, historico_chutes))}
Pontuação Final: {pontos}
Desempenho: {'👍' if pontos > 500 else '👎'}
""")
Cores
Personalize com cores para ficar mais amigavel
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'  # volta para a cor padrão

print(f"{GREEN}Parabéns, você acertou!{RESET}")
print(f"{RED}Errou! Tente novamente.{RESET}")

## 💡 Dicas para Implementação
1. Comece pelos desafios de Nível 1
2. Teste cada modificação isoladamente
3. Use comentários `#` para anotar suas alterações
4. Para listas (histórico), inicie com:  
```python
historico_chutes = []  # No início do programa
historico_chutes.append(chute)  # Dentro do loop
    