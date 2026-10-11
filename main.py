# Disciplina LFA Professora: Amanda Gordin de Oliveira
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

def ler_entrada(prompt, valor_padrao=None):
    print(prompt, end="")
    try:
        valor = input()
        if valor == "":
            if valor_padrao is not None:
                print(f"(uso padrão: {valor_padrao})")
                return valor_padrao
            return valor
        return valor
    except EOFError:
        if valor_padrao is not None:
            print(f"(uso padrão: {valor_padrao})")
            return valor_padrao
        return ""


estados = []
alfabeto = []
func_transicao = {}
estado_inicial = ""
estados_aceitacao = []

# recebendo os dados do autômato
estados = ler_entrada("Informe o conjunto de estados: ", "q0 q1").split()
alfabeto = ler_entrada("Informe o conjunto de alfabeto de entrada: ", "0 1").split()
estado_inicial = ler_entrada("Informe o estado inicial: ", "q0").strip()
estados_aceitacao = ler_entrada("Informe o estado aceitação: ", "q1").split()

print("Defina as funções de transição:")
for estado in estados:
    for simbolo in alfabeto:
        print(f"\t {simbolo} ")
        print(f"{estado} \t --------->\t", end="")
        proximo_estado = ler_entrada("", "q1")

        if proximo_estado == ".":
            func_transicao[(estado, simbolo)] = None
        else:
            func_transicao[(estado, simbolo)] = proximo_estado.strip()

# reconhecer linguagens
entrada = ler_entrada("Informe a linguagem a ser reconhecida: ", "01")

estado_atual = estado_inicial
aceito = True

for simbolo in entrada:
    proximo_estado = func_transicao.get((estado_atual, simbolo))

    if proximo_estado is None:
        aceito = False
        break

    estado_atual = proximo_estado

aceito = aceito and estado_atual in estados_aceitacao

if aceito:
    print("Reconhecido")
else:
    print("Não Reconhecido")

