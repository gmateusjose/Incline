import matplotlib as mpl
import matplotlib.pyplot as plt

from math import sin, cos, radians, sqrt, ceil, degrees, atan
from checking import get_data

# System configuration
QTY_ARGUMENTS = 5
GRAV = 9.82

# Sytem arguments
DATA = get_data(QTY_ARGUMENTS)

# Axis and some plotting configuration
PLOT_CONFIG = dict()

# lambda functions to make sin and cos accept entries in degrees
dsin = lambda deg_angle: sin(radians(deg_angle))
dcos = lambda deg_angle: cos(radians(deg_angle))

def main():
    # Configuring the plot
    mpl.rcParams['font.family'] = 'serif'

    # Changing things accordingly with the graph mode
    if 'fixedLength' in DATA.keys():
        plt.xlabel('Ângulo [Graus]')
        PLOT_CONFIG['starting_angle'] = 5
        PLOT_CONFIG['ending_angle'] = 85

        xvalues = [x for x in range(PLOT_CONFIG['starting_angle'], \
            PLOT_CONFIG['ending_angle'] + 1)]
        
        sliding = (lambda xvalues: {'x': xvalues, 'y': [sliding_model(x) for x in \
            xvalues]})(xvalues)
        rolling = (lambda xvalues: {'x': xvalues, 'y': [rolling_model(x) for x in \
            xvalues]})(xvalues)
        
        friction = get_friction()
        compression = get_compression()
        
    else:
        plt.xlabel('Comprimento rampa [m]')
        PLOT_CONFIG['starting_length'] = 0.5
        PLOT_CONFIG['ending_length'] = 1.5
        
        xvalues = [x/20 for x in range(int(PLOT_CONFIG['starting_length'] + 1), \
            int(PLOT_CONFIG['ending_length'] * 20 + 1))]

        sliding = (lambda xvalues: {'x': xvalues, 'y': [sliding_model(x) for x in \
            xvalues]})(xvalues) 
        friction = (lambda xvalues: {'x': xvalues, 'y': [friction_model(x) for x in \
            xvalues]})(xvalues)
        rolling = (lambda xvalues: {'x': xvalues, 'y': [rolling_model(x) for x in \
            xvalues]})(xvalues)
        compression = (lambda xvalues: {'x': xvalues, 'y': [compression_model(x) for \
            x in xvalues]})(xvalues)
    
    # Ploting the line graphs
    plt.plot(sliding['x'], sliding['y'], label='Deslizamento')
    plt.plot(friction['x'], friction['y'], \
        label=rf"Fricção ($\mu = {DATA['friction']}$)")
    plt.plot(rolling['x'], rolling['y'], label='Rolamento')
    plt.plot(compression['x'], compression['y'], \
        label=rf"Compressão ($\alpha = {DATA['rolling']}$)")

    # Plotting the y-axis, the scatter plot (if any) the legend and showing up
    # the graph
    plt.scatter(DATA['scatter']['x'], DATA['scatter']['y'], c='black', \
        label="Resultado experimental")
    plt.ylabel('Duração movimento [s]')
    plt.legend()
    plt.show()


# Calculation Functions 
def sliding_model(entry):
    if 'fixedLength' in DATA.keys():
        num = 2 * DATA['fixedLength']
        den = GRAV * dsin(entry)
    else:
        num = 2 * entry
        den = GRAV * dsin(DATA['fixedAngle'])
    return sqrt(num / den)

def friction_model(entry):
    if 'fixedLength' in DATA.keys():
        num = 2 * DATA['fixedLength']
        den = GRAV * (dsin(entry) - DATA['friction'] * dcos(entry))
    else:
        num = 2 * entry
        den = GRAV * (dsin(DATA['fixedAngle']) - DATA['friction'] * \
            dcos(DATA['fixedAngle']))
    return sqrt(num / den)

def rolling_model(entry):
    if 'fixedLength' in DATA.keys():
        num = 2.8 * DATA['fixedLength']
        den = GRAV * dsin(entry)
    else:
        num = 2.8 * entry
        den = GRAV * dsin(DATA['fixedAngle'])
    return sqrt(num / den)

def compression_model(entry):
    if 'fixedLength' in DATA.keys():
        num = 2.8 * DATA['fixedLength']
        den = GRAV * (dsin(entry) - DATA['rolling'] * dcos(entry))
    else:
        num = 2.8 * entry
        den = GRAV * (dsin(DATA['fixedAngle']) - DATA['rolling'] * \
            dcos(DATA['fixedAngle']))
    return sqrt(num / den)

def get_compression():
    starting_angle = ceil(degrees(atan(DATA['rolling'])))
    if starting_angle <= PLOT_CONFIG['starting_angle']:
        starting_angle = PLOT_CONFIG['starting_angle']

    xvalues = [x for x in range(starting_angle, PLOT_CONFIG['ending_angle'] + 1)]
    return {'x': xvalues, 'y': [compression_model(x) for x in xvalues]}

def get_friction():
    # Getting the xvalues who satisfy the condition
    starting_angle = ceil(degrees(atan(DATA['friction'])))
    if starting_angle < PLOT_CONFIG['starting_angle']:
        starting_angle = PLOT_CONFIG['starting_angle']

    xvalues = [x for x in range(starting_angle, PLOT_CONFIG['ending_angle'] + 1)]
    return {'x': xvalues, 'y': [friction_model(x) for x in xvalues]}

main()
