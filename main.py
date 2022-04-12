def transformListAdjacency(data, n):
    listaDeAdjacencias = []
    for i in range(n):
        arrayTemp = []
        for j in range(len(data)):
            if(data[j][0] == i+1):
                arrayTemp.append(data[j][1])
        listaDeAdjacencias.append(arrayTemp)
    return listaDeAdjacencias

def componenteConexa(checkVerticesPath, interacao):
    component = []
    for check in range(len(checkVerticesPath)):
        if(checkVerticesPath[check] == interacao):
            component.append(check + 1)
    return component

def verificaSeExisteOutraComponent(checkVerticesPath):
    for i in range(len(checkVerticesPath)):
        if(checkVerticesPath[i] == -1):
            return True
    return False

def findProximaComponenteConexa(checkVerticesPath):
    for i in range(len(checkVerticesPath)):
        if(checkVerticesPath[i] == -1):
            return i + 1

def buscaEmProfundidade(listaDeAdjacencias):
    checkVerticesPath = []
    before = []
    next = []

    for i in range(n):
        checkVerticesPath.append(-1)    

    origin = 1
    before.append(origin)

    componentes = []
    interacao = 1

    while(verificaSeExisteOutraComponent(checkVerticesPath)):
        while (len(before) != 0):
            itemRemove = before[0]
            before.remove(itemRemove)
            checkVerticesPath[itemRemove - 1] = interacao
            if(len(listaDeAdjacencias[itemRemove - 1]) > 0):
                for i in range(len(listaDeAdjacencias[itemRemove - 1])):
                    vertice = listaDeAdjacencias[itemRemove - 1][i]
                    if(checkVerticesPath[vertice - 1] == -1):
                        next.append(vertice)
                        checkVerticesPath[vertice - 1] = interacao
                if (len(before) == 0):
                    temp = before
                    before = next
                    next = temp
        componentes.append(componenteConexa(checkVerticesPath, interacao))
        interacao += 1
        before.append(findProximaComponenteConexa(checkVerticesPath))
    return componentes


# Observar qual o erro para essa instância
# Entrada
data = [[2,9], [3, 8], [5, 7], [6,9], [8,10]]
n = 10

checkVerticesPath = []

listaDeAdjacencias = transformListAdjacency(data, n)
buscaProfundidade = buscaEmProfundidade(listaDeAdjacencias)
print(buscaProfundidade)

