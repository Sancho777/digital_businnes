# Problema  - A_cordes I_ntergaláticos
# 
# --- Input ---
# A primeira linha da entrada contém dois inteiros, N (2 <= N <= 100000), e Q (1 <= Q <= 100000),
# respectivamente o número de teclas do piano intergalático e a quantidade de acordes. As Q linhas
# seguintes contêm, cada uma, dois inteiros A e B, (0 <= A < B < n), representando um acorde.
# 
# --- Output ---
# Seu programa deve imprimir N inteiros, um por linha, representando as notas associadas às teclas
# do piano, após todos os acordes terem sido tocados
# 
# --- Exemplo ---
#   - Entrada -     - Saída -
#       5 3             5
#       1 2             6
#       0 4             6
#       0 2             2
#                       2

# nq = Escreva o número de teclas do piano intergalático e a quantidade de acordes.
nq = input().split(' ')
N = []  # Número de teclas do piano intergalático.
Q = []  # Quantidade de acordes.


def nota_mais_frequente(acorde):
    # Retorna o elemento mais frequente de um acorde.
    maior = 0
    count = 0
    for i in acorde:
        if (acorde.count(i) > count):
            maior = i
            count = acorde.count(i)
        elif (acorde.count(i) == count):
            if i > maior:
                maior = i
                count = acorde.count(i)
    # print(maior)
    return maior


for elemento in range(int(nq[0])):
    N.append(1)

for elemento in range(int(nq[1])):
    nota = input().split(' ')
    Q.append([int(nota[0]), int(nota[1])])

for nota in Q:
    first = nota[0]
    last = nota[1]
    nota_nova = nota_mais_frequente(N[first:last+1])
    while first <= last:
        N[first] += nota_nova
        if N[first] >= 9:
            N[first] -= 9
        first += 1

for i in N:
    print(i)