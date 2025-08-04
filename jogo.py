import random

print("{{{{{{{{{{{{{{{{!}}}}}}}}}}}}}}}}")
print("{{{                           }}}")
print("{{     JOGO DE ADIVINHAÇÃO     }}")
print("{              DO               }")
print("{{       Pietro Henrique       }}")
print("{{{                           }}}")
print("{{{{{{{{{{{{{{{{!}}}}}}}}}}}}}}}}")

numeroSecreto = random.randrange(0,100)
totalTentativas = 0 
pontos = 100

print("Qual niveis de dificuldade ? ")
print("(1)- Facíl (2)- Médio (3)- Difícil ")

nivel = int(input("Escolha um nivel "));

if (nivel == 1):
    print("20 tentativas!! Ta com medo, seu pinto 😂")
elif (nivel == 2):
    print("15 tentativas!! Ta começando a me impresionar 🗿")
else:
    print("10 tentativas!! Você é o sigma supremo 🐺🖤⛓️💔")


for radada in range (1, totalTentativas +1):
    print("tentativa {} de {}" . format(radada,totalTentativas) )
    chute_str = input("Digite um número entre 1 e 100: ")
    chute = int(chute_str)

    if (chute < 1 or > 100):
        print("Número invalido")
        continue

    acertou = chute == numeroSecreto
    maior = chute > numeroSecreto
    menor = chute < numeroSecreto1q 

