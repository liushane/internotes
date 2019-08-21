import numpy as np
import matplotlib.pyplot as plt

DNA_SIZE = 10           #DNA length
POP_SIZE = 100          #population size
CROSS_RATE = 0.8        #mating probability (DNA crossover)
MUTATION_RATE = 0.003   #mutation probability
N_GENERATIONS = 200
X_BOUND = [0,5]         #x upper and lower bounds

#
def F(x):
    #to find the maximum
    return np.sin(10*x)*x + np.cos(2*x)*x


#适应度
def get_fitness(pred):
    return pred+1e-3 - np.min(pred)

#将编码后的ＤＮＡ翻译回来(解码)
def translateDNA(pop):
    return pop.dot(2**np.arange(DNA_SIZE)[::-1]/(2**DNA_SIZE-1)*X_BOUND[1])

#自然选择
def select(pop,fitness):
    idx = np.random.choice(np.arange(POP_SIZE),size=POP_SIZE,
                           replace=True,p=fitness/fitness.sum())
    return pop[idx]

#染色体交叉
def crossover(parent,pop):
    if np.random.rand() < CROSS_RATE:
        i_ = np.random.randint(0,POP_SIZE,size=1)
        cross_points = np.random.randint(0,2,size=DNA_SIZE).astype(np.bool)
        parent[cross_points]=pop[i_,cross_points]
        return parent

def mutate(child):
    for point in range(DNA_SIZE):
        if np.random.rand()<MUTATION_RATE:
            child[point]=1 if child[point]==0 else 0
    return child

pop = np.random.randint(0,2,(1,DNA_SIZE)).repeat(POP_SIZE,axis=0)

for _ in range(N_GENERATIONS):
    F_values = F(translateDNA(pop))
    fitness = get_fitness(F_values)
    pop = select(pop,fitness)
    pop_copy = pop.copy()
    for parent in pop:
        child = crossover(parent,pop_copy)
        child = mutate(child)
        parent[:] = child


print(pop.dot(2**np.arange(DNA_SIZE)[::-1]/(2**DNA_SIZE-1)*X_BOUND[1]))
# print(np.random.randint(0,2,(1,DNA_SIZE)))