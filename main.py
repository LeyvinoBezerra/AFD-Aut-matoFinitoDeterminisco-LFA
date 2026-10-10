# Disciplina LFA Professora: Amanda Gordin de Oliveira
from xml.dom import NoModificationAllowedErr

# AFD - Autômato Finito Determinisco

# M = {Q, Σ, δ, q0, F}

# Q = {q0,q1}
# Σ = {0, 1}

# δ = {
#       δ: (q0, 0) -> q1,
#       δ: (q0, 1) -> q1,
#       δ: (q0, 0) -> q1,
#       δ: (q0, 1) -> q1
#      }

# q0 = q0
# F  = {q1}

# definindo as estruturas

estados = []
alfabeto = []
func_transicao = {}
estado_inicial = ""
estados_aceitação = []

# recebendo os dados do autômato
print("Informe o conjunto de estados: ", end="")
estados = input().split()

print("Informe o conjunto de alfabeto de entrada: ", end="")
alfabeto = input().split()

print("Informe o estado inicial: ", end="")
estado_inicial = input().split()

print("Informe o estado aceitação: ", end="")
estados_aceitação = input().split()

print("Defina as funções de transição:")
for estado in estados:
    for simbolo in alfabeto:
        print(f"\t {simbolo} ")
        print(f"{estado} \t --------->\t", end="")
        proximo_estado = input()

        if proximo_estado == ".":
            func_transicao[(estado, simbolo)] = None
        else:
            func_transicao[(estado, simbolo)] = proximo_estado
# reconhecer linguagens
print("Informe a linguagem a ser reconhecida: ", end="")
entrada = input()

estado_atual = estado_inicial

for simbolo in alfabeto:
    print(f"Estado atual: {estado_atual}")
    print(f"Estado atual: {simbolo}")

    print(f"Proximo estado: {func_transicao[(estado_atual, simbolo)]}")

    estado_atual = func_transicao[(estado_atual, simbolo)]

    if estado_atual == None:
        print("O automato não reconheceu a linguagem")
        break

    if estado_atual in estados_aceitação:
        print("Reconhecido")
    else:
        print("Não Reconhecido")




