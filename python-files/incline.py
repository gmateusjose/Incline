import matplotlib as mpl
import matplotlib.pyplot as plt

from math import sin, cos, radians, sqrt 
from checking import get_data

QTY_ARGUMENTS = 5
GRAV = 9.82 # Measurement made with smartphone


def main():
    data = get_data(QTY_ARGUMENTS)

    # Configuring the plot
    mpl.rcParams['font.family'] = 'serif'

    # Changing things accordingly with the graph mode

    if 'fixedLength' in data.keys():
        plt.xlabel('Ângulo [Graus]')

        sliding = get_sliding(data['fixedLength'])
        rolling = get_rolling(data['fixedLength'], data['friction'])
    else:
        plt.xlabel('Comprimento rampa [m]')
    
    # Ploting the line graphs
    plt.plot(sliding['x'], sliding['y'], label='Deslizamento')
    plt.plot([1, 2, 3, 4], [2, 4, 6, 8], \
        label=rf"Fricção ($\mu = {data['friction']}$)")
    plt.plot(rolling['x'], rolling['y'], label='Rolamento')
    plt.plot([1, 2, 3, 4], [4, 8, 12, 16], \
        label=rf"Compressão ($\alpha = {data['rolling']}$)")

    # Plotting the y-axis, the scatter plot (if any) the legend and showing up
    # the graph
    plt.scatter(data['scatter']['x'], data['scatter']['y'], c='black')
    plt.ylabel('Duração movimento [s]')
    plt.legend()
    plt.show()


def get_sliding(fixed_length):
    # Getting the xvalues between 1 and 85 with step 5
    xvalues = [x for x in range(10, 90)]
    yvalues = list()

    for x in xvalues:
        num = 2 * fixed_length
        den = GRAV * sin(radians(x))
        print(f"{x}, {sqrt(num / den)}")
        yvalues.append(sqrt(num / den))
    return {'x': xvalues, 'y': yvalues}


def get_rolling(fixed_length, friction):
    # Getting the xvalues who satisfy the condition
    xvalues = [x for x in range(10, 90)]
    yvalues = list()
    
    for x in xvalues:
        num = 2 * fixed_length
        den = GRAV * (sin(radians(x)) - friction * cos(radians(x))) 
        try:
            yvalues.append(sqrt(num / den))
        except:
            yvalues.append(0)

    return {'x': xvalues, 'y': yvalues}

main()
