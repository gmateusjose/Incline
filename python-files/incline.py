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
        friction = get_friction(data['fixedLength'], data['friction'])
        rolling = get_rolling(data['fixedLength'])
        compression = get_compression(data['fixedLength'], data['rolling']) 
    else:
        plt.xlabel('Comprimento rampa [m]')
    
    # Ploting the line graphs
    plt.plot(sliding['x'], sliding['y'], label='Deslizamento')
    plt.plot(friction['x'], friction['y'], \
        label=rf"Fricção ($\mu = {data['friction']}$)")
    plt.plot(rolling['x'], rolling['y'], label='Rolamento')
    plt.plot(compression['x'], compression['y'], \
        label=rf"Compressão ($\alpha = {data['rolling']}$)")

    # Plotting the y-axis, the scatter plot (if any) the legend and showing up
    # the graph
    plt.scatter(data['scatter']['x'], data['scatter']['y'], c='black')
    plt.ylabel('Duração movimento [s]')
    plt.legend()
    plt.show()


def get_compression(fixedLength, rolling):
    xvalues = [x for x in range(10, 90)]
    yvalues = list()
    
    for x in xvalues:
        try:
            num = 2.8 * fixedLength
            den = GRAV * (sin(radians(x)) - rolling*cos(radians(x)))
            yvalues.append(sqrt(num / den))
        except:
            yvalues.append(0)

    return {'x': xvalues, 'y': yvalues}

def get_rolling(fixedLength):
    xvalues = [x for x in range(10, 90)]
    yvalues = list()

    for x in xvalues:
        num = 2.8 * fixedLength 
        den = GRAV * sin(radians(x))
        yvalues.append(sqrt(num / den))
    return {'x': xvalues, 'y': yvalues}


def get_sliding(fixed_length):
    # Getting the xvalues between 1 and 85 with step 5
    xvalues = [x for x in range(10, 90)]
    yvalues = list()

    for x in xvalues:
        num = 2 * fixed_length
        den = GRAV * sin(radians(x))
        yvalues.append(sqrt(num / den))
    return {'x': xvalues, 'y': yvalues}


def get_friction(fixed_length, friction):
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
