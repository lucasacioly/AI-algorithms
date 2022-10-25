class Matrix:
    # Initialize the class
    def __init__(self,fill,row,column):
        self.matrix = []
        self.row = row
        self.column = column
        for i in range(0,self.row+1):
            self.matrix.append([])
            for j in range(0,self.column+1):
                self.matrix[i].append(fill)


    def setValue(self, i, j, wt):
        self.matrix[i][j] = wt

    def delValue(self, i, j):
        self.matrix[i][j] = 0

    def getValue(self, i, j):
        return self.matrix[i][j]

    def seeMatrix(self):
        print('\n'.join(['  '.join(['{:8}'.format(f"{item:.2f}") for item in row[1:]]) for row in self.matrix[1:]]))


#Função de atualização de valor
def atualizaValor(estado, acao, proximoEstado, recompensa, q_matriz , alfa, gama):
    estimativa = recompensa.getValue(estado, proximoEstado) + gama * max(q_matriz.getValue(proximoEstado,1),q_matriz.getValue(proximoEstado,2),q_matriz.getValue(proximoEstado,3),q_matriz.getValue(proximoEstado,4))

    q_matriz.setValue(estado,acao,q_matriz.getValue(estado,acao) + alfa*(estimativa - q_matriz.getValue(estado,acao)))

#PRINT POLÍTICA
def seePolitica(vetor):
    actions = ["UP", "DW", "LF", "RG"]
    array = []
    for estado in vetor[1:6]:
        estado = estado[1:]
        array.append(actions[estado.index(max(estado))])

    print(f'''\nPolitica:  
{array[4]} 1
{array[2]} {array[3]}
{array[0]} {array[1]}
        ''')
    


def main():
#Inicialização da matriz Q
    q_matriz = Matrix(0,6,4)

    q_matriz.setValue(6, 1, 1)
    q_matriz.setValue(6, 2, 1)
    q_matriz.setValue(6, 3, 1)
    q_matriz.setValue(6, 4, 1)

    


    alfa = 0.5
    gama = 1

    recompensa = Matrix(0,5,6)
    
    recompensa.setValue(1,1,-10)
    recompensa.setValue(1,2,-1)
    recompensa.setValue(1,3,-1)

    recompensa.setValue(2,1,-1)
    recompensa.setValue(2,2,-10)
    recompensa.setValue(2,4,-1)

    recompensa.setValue(3,1,-1)
    recompensa.setValue(3,3,-10)
    recompensa.setValue(3,5,-1)
    recompensa.setValue(3,5,-1)

    recompensa.setValue(4,2,-1)
    recompensa.setValue(4,3,-1)
    recompensa.setValue(4,4,-10)
    recompensa.setValue(4,6,10)

    recompensa.setValue(5,5,-10)
    recompensa.setValue(5,3,-1)
    recompensa.setValue(5,6,10)

    '''
    UP - 1
    DOWN - 2
    LEFT - 3
    RIGHT - 4

    '''

#ARMAZENAMENTO DE TRAJETÓRIAS
    trajetoria1 = [[1,1,2],[2,2,2],[2,4,2],[2,3,1],[1,4,3],[3,3,3],[3,3,3],[3,1,5],[5,4,6]]
    trajetoria2 = [[1,1,3],[3,1,5],[5,3,3],[3,3,3],[3,3,5],[5,4,6]]
    trajetoria3 = [[1,2,1],[1,1,3],[3,4,5],[5,1,5],[5,2,5],[5,3,5],[5,2,3],[3,1,5],[5,4,5],[5,4,6]]
    trajetoria4 = [[1,1,3],[3,4,4],[4,1,6]]
    trajetoria5 = [[1,3,1],[1,1,1],[1,1,3],[3,1,5],[5,3,5],[5,2,3],[3,1,5],[5,1,5],[5,1,5],[5,2,3],[3,1,3],[3,3,3],[3,4,4],[4,1,6]]

#PERCORRENDO TRAJETÓRIAS
    for i in trajetoria1:
        atualizaValor(i[0],i[1],i[2],recompensa,q_matriz,alfa,gama)

    for i in trajetoria2:
        atualizaValor(i[0],i[1],i[2],recompensa,q_matriz,alfa,gama)
    
    for i in trajetoria3:
        atualizaValor(i[0],i[1],i[2],recompensa,q_matriz,alfa,gama)

    for i in trajetoria4:
        atualizaValor(i[0],i[1],i[2],recompensa,q_matriz,alfa,gama)

    for i in trajetoria5:
        atualizaValor(i[0],i[1],i[2],recompensa,q_matriz,alfa,gama)

    #PRINT Q-MATRIX E POLÍTICA
    print("Q - Matrix")
    q_matriz.seeMatrix()
    seePolitica(q_matriz.matrix)

    
if __name__ == "__main__": main()
