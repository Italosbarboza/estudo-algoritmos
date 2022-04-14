def transformListAdjacency(data, n):
    adjacencyList = []
    for i in range(n):
        arrayTemp = []
        for j in range(len(data)):
            if(data[j][0] == i+1):
                arrayTemp.append(data[j][1])
            elif(data[j][1] == i+1):
                arrayTemp.append(data[j][0])
        adjacencyList.append(arrayTemp)
    return adjacencyList

def connectedComponent(checkVerticesPath, iteration):
    component = []
    for check in range(len(checkVerticesPath)):
        if(checkVerticesPath[check] == iteration):
            component.append(check + 1)
    return component

def verifyNextConnectedComponent(checkVerticesPath):
    for i in range(len(checkVerticesPath)):
        if(checkVerticesPath[i] == -1):
            return True
    return False

def findNextConnectedComponent(checkVerticesPath):
    for i in range(len(checkVerticesPath)):
        if(checkVerticesPath[i] == -1):
            return i + 1

def widthSearch(listaDeAdjacencias):
    checkVerticesPath = []
    before = []
    next = []

    for i in range(n):
        checkVerticesPath.append(-1)    

    origin = 1
    before.append(origin)

    component = []
    iteration = 1

    while(verifyNextConnectedComponent(checkVerticesPath)):
        while (len(before) != 0):
            itemRemove = before[0]
            before.remove(itemRemove)
            checkVerticesPath[itemRemove - 1] = iteration
            if(len(listaDeAdjacencias[itemRemove - 1]) > 0):
                for i in range(len(listaDeAdjacencias[itemRemove - 1])):
                    vertice = listaDeAdjacencias[itemRemove - 1][i]
                    if(checkVerticesPath[vertice - 1] == -1):
                        next.append(vertice)
                        checkVerticesPath[vertice - 1] = iteration
                if (len(before) == 0):
                    temp = before
                    before = next
                    next = temp
        component.append(connectedComponent(checkVerticesPath, iteration))
        iteration += 1
        before.append(findNextConnectedComponent(checkVerticesPath))
    return component


data = []
n = 0
i = 0

while True:
    try:
        line = input()
        i = i + 1
    except EOFError:
        break
    if(i==3):
        n = int(line.split('=')[1])
    if(i>4):
        graph = [int(item) for item in line.split()]
        data.append(graph)

checkVerticesPath = []

adjacencyList = transformListAdjacency(data, n)
graphWidth = widthSearch(adjacencyList)
for i in range(len(graphWidth)):
    print(*graphWidth[i])
