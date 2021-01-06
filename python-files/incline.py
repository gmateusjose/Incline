import matplotlib as mpl
import matplotlib.pyplot as plt

from math import sin, cos, radians, sqrt 
from checking import get_data

QTY_ARGUMENTS = 5
GRAV = 9.18


def main():
    data = get_data(QTY_ARGUMENTS)

    # Configuring the plot
    mpl.rcParams['font.family'] = 'serif'

    # Changing things accordingly with the graph mode
    if data['mode'] == 'length':
        plt.xlabel('Ângulo [Graus]')
    else:
        plt.xlabel('Comprimento rampa [m]')
    
    # Ploting the line graphs
    plt.plot([1, 2, 3], [1, 2, 3], label='Deslizamento')
    plt.plot([1, 2, 3], [2, 4, 6], \
        label=rf"Fricção ($\mu = {data['friction']}$)")
    plt.plot([1, 2, 3], [3, 6, 9], label='Rolamento')
    plt.plot([1, 2, 3], [4, 8, 12], \
        label=rf"Compressão ($\alpha = {data['rolling']}$)")

    # Plotting the y-axis, the scatter plot (if any) the legend and showing up
    # the graph
    plt.scatter(data['scatter']['x'], data['scatter']['y'], c='black')
    plt.ylabel('Duração movimento [s]')
    plt.legend()
    plt.show()

"""
def plot_length():
    x = [x for x in range(10, 90, 5)]
    y_deslizamento = []
    y_friccao = []
    y_rotacao = []
    y_compressao = []

    for angle in x:
        deslizamento = sqrt(2*argv[2] / G*sin(radians(angle)))
        friccao = 
        rotacao =
        compressao =
        
        y_deslizamento.append(deslizamento)
        y_friccao.append(friccao)
        y_rotacao.append(rotacao)
        y_compressao.append(compressao)
        
def plot_angle():
    x = [x/10 for x in range(16)]
    y_deslizamento = []
    y_friccao = []
    y_rotacao = []
    y_compressao = []

    for length in x:
        deslizamento = sqrt(2*length / G*sin(radians(argv[2])))
        friccao = sqrt(2*length / G*(sin(radians(argv[2])) - \
            cos(radians(argv[2]))))
        rotacao = sqrt()
        compressao = sqrt()

        y_deslizamento.append(deslizamento)
        y_friccao.append(friccao)
        y_rotacao.append(rotacao)
        y_compressao.append(compressao)
"""
main()
