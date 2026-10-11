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
# Exemplo de AFD (Autômato Finito Determinístico)

# M = {Q, Σ, δ, q0, F}

# Conjunto de estados
# Q = {q0, q1, q2}

# Alfabeto
# Σ = {a, b}

# Função de transição δ:
#q1

# Estado inicial
# q0 = q0

# Conjunto de estados finais
# F = {q2}

# Esse autômato aceita todas as palavras que terminam com "ab".
# Exemplos aceitos: "ab", "aab", "bbbab", "aaab"
# Exemplos não aceitos: "aaa", "bbb", "ba"
# Exemplo de AFD (Autômato Finito Determinístico)
# Não Aceito
# Exemplo de AFD (Autômato Finito Determinístico)
#
# M = {Q, Σ, δ, q0, F}
#
# Conjunto de estados:
# Q = {q0, q1, q2}
#
# Alfabeto:
# Σ = {a, b}
#
# Função de transição δ:
# δ(q0, a) -> q1
# δ(q0, b) -> q0
# δ(q1, a) -> q1
# δ(q1, b) -> q2
# δ(q2, a) -> q2
# δ(q2, b) -> q2
#
# Estado inicial:
# q0 = q0
#
# Conjunto de estados finais:
# F = {q2}
#
# Esse autômato aceita todas as palavras que terminam com "ab".
#
# Exemplos de palavras ACEITAS:
# "ab"     -> q0 --a--> q1 --b--> q2 (final)
# "aab"    -> q0 --a--> q1 --a--> q1 --b--> q2 (final)
# "bbbab"  -> q0 --b--> q0 --b--> q0 --b--> q0 --a--> q1 --b--> q2 (final)
# "aaab"   -> q0 --a--> q1 --a--> q1 --a--> q1 --b--> q2 (final)
#
# Exemplos de palavras NÃO ACEITAS:
# "aaa"    -> q0 --a--> q1 --a--> q1 --a--> q1 (termina em q1, não final)
# "bbb"    -> q0 --b--> q0 --b--> q0 --b--> q0 (termina em q0, não final)
# "ba"     -> q0 --b--> q0 --a--> q1 (termina em q1, não final)


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

