# Dados de entrada
pesos = [1, 2, 3, 4, 5] 
valores = [5, 4, 6, 1, 3]  
PESO_MAXIMO = 22  
LIMITE_PESO = int(0.35 * PESO_MAXIMO) # Limite de 35% do peso por item
PESO_PENALIDADE = int(0.2 * PESO_MAXIMO) # Capacidade com aplique de penalidade

# A lógica se baseia em criar um indice sobre a relação valor/peso
# Para isso, utilizei tuplas (possui mais performance que a lista ao custo de ser imútavel)
# Cada tupla contém a relação valor/peso, junto dos dados e do índice da operação
# O python também nos permite criar listas de forma dinâmica com o for dentro dela
itens = [(valores[i] / pesos[i], pesos[i], valores[i], i) for i in range(len(pesos))]

# Agora nos ordenamos os itens do maior para o menor (reverse=True)
# Um ponto importante é o parámetro key, que indicara o elemento que será a base para a ordenação
# O elemento usado para ordenar neste caso, é a relação valor/peso
itens.sort(reverse=True, key=lambda x: x[0])


# Esta função não ultrapasa o limite de estabelecido
def nao_ultrapassa_limite(itens):
    # Valores totais
    peso_total = 0
    valor_total = 0

    # Adicionar os itens na mochila, iterando sobre o array com os respectivos valores das tuplas
    for _, peso, valor, i in itens:
        peso_acumulado = 0

        # Adicionado o mesmo item até não couber mais, no fim ele passará para o próximo item no array
        while peso_total + peso <= PESO_MAXIMO:
            # Verificando se o peso não passará o limite, se passar do limite, passsará para o próximo item
            if peso_acumulado + peso >= LIMITE_PESO:
                break
            else:
                peso_total += peso
                valor_total += valor
                peso_acumulado += peso
    
    return peso_total, valor_total


# Esta função ultrapassa o limite estabelecido, diminuindo a capacidade da mochila
def ultrapassa_limite(itens):
    # Valores totais
    peso_total = 0
    valor_total = 0
    
    # Valor que define a capacidade total para controlar a redução
    capacidade_atual = PESO_MAXIMO
    penalidade = False

    # Adicionar os itens na mochila, iterando sobre o array com os respectivos valores das tuplas
    for _, peso, valor, i in itens:
        peso_acumulado = 0

        # Adicionado o mesmo item até não couber mais, no fim ele passará para o próximo item no array
        while peso_total + peso <= capacidade_atual:
            peso_total += peso
            valor_total += valor
            peso_acumulado += peso

        # Este trecho aplicara a penalidade, porém apenas uma vez utilizando a variavel penalidade
        if peso_acumulado > LIMITE_PESO and not penalidade:
            capacidade_atual = PESO_PENALIDADE
            penalidade = True
    
    return peso_total, valor_total

#Exibir os resultados
peso_total1, valor_total1  = nao_ultrapassa_limite(itens)
print(f'---Sem ultrapassar a penalidade---')
print(f'Peso total na mochila: {peso_total1}, valor total na mochila: {valor_total1} \n')

peso_total2, valor_total2  = ultrapassa_limite(itens)
print(f'---Ultrapassando a penalidade---')
print(f'Peso total na mochila: {peso_total2}, valor total na mochila: {valor_total2}')
