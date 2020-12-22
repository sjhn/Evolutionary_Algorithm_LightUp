import yaml
import random
import numpy as np

def config_reader(d):
    data = yaml.load(d, Loader=yaml.FullLoader)
    black_cell_constraint = data['black_constraint']
    logs = data['logs']
    evals = data['evaluations']
    #problem_instance_pathname = data['problem_instance_pathname']
    solution_file_pathname = data['solution_file_pathname']
    random.seed(data['random_seed'])
    log_file_pathname = data['log_file_pathname']
    mu=data['mu']
    runs=data['runs']
    lambdaa=data['lambda']
    generations=data['generations']
    sbc=data['semi_black_constraint']
    stp=data['stochastic_parent']
    l = open(log_file_pathname, "w+")
    l.write('Result Log' + '\n')

    #l.write('\n' + 'Logs: \t' + str(data['logs']))
    #l.write('\n' + 'Evaluations:  \t' + str(data['evaluations']))
    #l.write('\n' + 'Random seed: \t' + str(data['random_seed']))
    #l.write('\n' + 'Log file path+name: \t' + str(data['log_file_pathname']))
    #l.write('\n' + 'Solution file path+name: \t' + str(data['solution_file_pathname']) + '\n')

    return black_cell_constraint, logs, evals, solution_file_pathname, l,mu,lambdaa,generations,sbc,stp,runs


def board_reader(x, y, f, o):
    # Initializing a board in which 0 represents
    # an empty cell and 1 represents a lamp
    board = np.zeros([int(x), int(y)])

    # Saving the positions of the black cells in
    # bc_board in which 0 represents an empty cell
    # and 2 represents a black cell
    bc_board = np.zeros_like(board) + 10
    black_list = []
    # Reading the input file
    line = f.readline()
    o.write(line)

    while line:
        xyz = line.split()
        xi = int(xyz[0])
        yi = int(xyz[1])
        zi = int(xyz[2])

        board[xi - 1, yi - 1] = 1
        bc_board[xi - 1, yi - 1] = zi

        line = f.readline()
        o.write(line)
        black_list.append([xi - 1, yi - 1])

    bc = board.sum()
    # counting the number of the white cells
    wc = x * y - bc
    # A list for saving each log's best solution
    return board, bc_board, black_list, bc, wc
