from sys import argv, exit


def get_data(arguments):
    # Checking if enough arguments were provided
    if not (len(argv) in [arguments, arguments + 1]):
        print("""
        Error: You must provide as arguments
        \t - a mode [-l/-a] (fixed length / fixed angle)
        \t - a fixed length or fixed angle value (depending on mode)
        \t - a friction constant
        \t - a rolling constant 
        \t - a filename to an experiment data (optional)
        """) 
        exit(1)

    # Checking if setup, fricition and rolling are valid numbers
    try:
        argv[2] = float(argv[2])
        argv[3] = float(argv[3])
        argv[4] = float(argv[4])
    except:
        print("""
        Error: Your setup, friction constant and rolling constant values must
        be numbers.
        """)
        exit(1)

    # Checking conditions for submitted values
    if not (argv[1] in ['-l', '-a']):
        print("""
        Error: You must provide a length mode (-l) or a angle mode(-a).
        """)
        exit(1)
    elif argv[1] == '-l' and argv[2] <= 0:
        print("""
        Error: You must provide a length greater than 0.
        """)
        exit(1)
    elif argv[1] == '-a' and (argv[2] <= 0 or argv[2] >= 90):
        print("""
        Error: You must provide an angle greater than 0 and lower than 90
        degrees.
        """)
        exit(1)
    elif argv[3] <= 0 or argv[4] <= 0:
        print("""
        Error: You must provide a friction constant and a rolling constant
        greater than 0.
        """)
        exit(1)
    
    # Checking for filename input

    # appending all the informations in a dict the mode by default is 'length'
    # but if an '-a' tag is added, the mode will change to 'angle'.
    experiment_data = {
        'friction': argv[3],
        'rolling': argv[4],
        'scatter': {'x': list(), 'y': list()}
    }
    if argv[1] == '-l':
        experiment_data['fixedLength'] = argv[2]
    else:
        experiment_data['fixedAngle'] = argv[2]

    return experiment_data
