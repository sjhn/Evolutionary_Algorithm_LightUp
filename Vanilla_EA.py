from sys import argv
import random
from Validation import random_bulb_placement, light_validity_check_and_fill, fitness_check
from mating import mate
from reading import config_reader, board_reader
import numpy as np
import matplotlib.pyplot as plt

from writing import write_solution


def main():
    if len(argv) == 3:
        print('The problem file passed is: {argv[1]}')
        print('The config file passed is: {argv[2]}')
        problem_file = argv[1]
        config_file = argv[2]
    elif len(argv) == 2:
        #print('oj')
        print('The problem file passed is: {argv[1]}')
        print('Using the default config file since none was specified!')
        problem_file = argv[1]
        config_file = 'Config.yaml'
    else:
        print('An inappropriate number of arguments were passed!')

    with open(config_file) as d:
        black_cell_constraint, logs, evals, solution_file_pathname, l,mu, lambdaa,generations, sbc,stp,runs = config_reader(d)
    # solution file
    o = open(solution_file_pathname, "w+")
    # input file
    f = open(problem_file)

    frl = f.readline()
    x = int(frl)
    o.write(frl)

    frl = f.readline()
    y = int(frl)
    o.write(frl)

    print(int(x))
    print(y)

    board, bc_board, black_list, bc, wc = board_reader(x, y, f, o)

    print('hi')
    # print(random_lamps)
    #initial_pool = []

    initial_pool=[]
    #mulan=mu+lambdaa

    for i in range(mu):
        valid, fitness, lightened,r_b = random_bulb_placement(black_cell_constraint,
                                                          bc_board, board, x, y, black_list, wc)

        initial_pool.append([r_b, fitness])


    pool=initial_pool.copy()


    conf=open(config_file)

    #runs=evals

    ev=0
    average_list=[]
    fittest_list=[]


    while ev<evals:
        for r in range(runs):
            l.write('\n'+'Run '+str(r))
            print('Run: '+str(r))
            for h in range(generations):
                #print('generation:',h)
                for num in range(lambdaa):
                    p1=random.randint(0,len(pool)-1)
                    p2=random.randint(0,len(pool)-1)

                    #print(p1,'p1')

                    #print(len(pool))
                    parent1=pool[p1]
                    #print(parent1)
                    parent2=pool[p2]

                    child=mate(parent1,parent2)
                    fitness = fitness_check(child,black_cell_constraint,bc_board,black_list,not sbc)[1]
                    ev+=1
                    #print(fitness)
                    pool.append([child,fitness])

                pool = sorted(pool, key=lambda x: x[1])[-mu:]
                #print(pool[-1][0])
                #print('average fitness:', (pool, lambda x: x[1][:]))
                sum=0
                for t in range (len(pool)):
                    #print(pool[t][1])
                    sum+=pool[t][1]
                #print('average:',sum/len(pool))
                avg=sum/len(pool)

                average_list.append(avg)
                fittest_list.append(pool[-1][1])
                l.write('\n'+str(mu+lambdaa*h)+'\t'+str(avg)+'\t'+str(pool[-1][1]))

    write_solution(o,pool[-1][0],pool[-1][1],x,y)

    plt.plot(average_list)
    #plt.show()
    plt.plot(fittest_list)
    plt.ylabel('fitness')
    plt.xlabel('evaluation')
    plt.title('mu:'+str(mu)+'\t'+'lambda:'+str(lambdaa)+'\n'+'black constraint considered:'
              +str(black_cell_constraint)+'\n'+'generations: '+str(generations)+'\t'+'black constraint penalty in fitness:'+str(sbc))
    #plt.figtext('figtext')
    plt.show()

if __name__ == '__main__':
    main()
