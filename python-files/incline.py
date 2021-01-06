import matplotlib as mpl
import matplotlib.pyplot as plt

from math import sin, cos, radians, sqrt 
from checking import get_data

QTY_ARGUMENTS = 5
GRAV = 9.18


def main():
    data = get_data(QTY_ARGUMENTS)
    print(data)

"""
def plot_length():
    mpl.rcParams['font.family'] = 'serif'
    plt.xlabel('Ângulo [Graus]')
    plt.ylabel('Duração movimento [s]')

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

    plt.plot(x, y_deslizamento, label='Deslizamento')
    plt.plot(x, y_friccao, label=r'Fricção com $\mu = $')
    plt.plot(x, y_rotacao, label='Rotação')
    plt.plot(x, y_compressao, label=r'Compressão com $\alpha = $')
    plt.legend()
    plt.show()

def plot_angle():
    mpl.rcParams['font.family'] = 'serif'
    plt.xlabel('Comprimento rampa [m]')
    plt.ylabel('Duração movimento [s]')

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

    plt.plot(x, y_deslizamento, label='Deslizamento')
    plt.plot(x, y_friccao, label=r'Fricção com $\mu = {}$'.format(argv[3]))
    plt.plot(x, y_rotacao, label='Rotação')
    plt.plot(x, y_compressao, label=r'Compressão com $\alpha = {}$'.format(argv[4]))
    plt.legend()
    plt.show()

def check_arguments():
    if len(argv) != NUMBER_OF_ARGUMENTS:
        print("Usage: python3.8 incline.py [-l/-a] [setup] [friction] [rolling].")
        exit(1)
    
    try:
        argv[2] = float(argv[2])
        argv[3] = float(argv[3])
        argv[4] = float(argv[4])
    except:
        print("Error: Your [setup], [friction] and [rolling] constants must be \
        numbers.")
        exit(1)

    if argv[1] != '-l' and  argv[1] != '-a':
        print("Error: You must provide a length mode (-l) or an angle mode (-a).")
        exit(1)
    elif argv[1] == '-l' and argv[2] <= 0:
        print("Error: You must provide length greater than 0.")
        exit(1)
    elif argv[1] == '-a' and (argv[2] <= 0 or argv[2] >= 90):
        print("Error: You must provide an angle greater than 0 and lower than \
        90 degrees.")
        exit(1)
    elif argv[3] <= 0 or argv[4] <= 0:
        print("Error: You must provide a [friction] constant and a [rolling] \
        constant greater than 0.")
        exit(1)

"""
main()
