import numpy as np
TARGET_PHRASE = 'You get it!'   #target DNA
POP_SIZE=300                    #population size
CROSS_RATE=0.4                  #mating probability (DNA crossover)
MUTATION_RATE=0.01              #mutation probability
N_GENERATIONS=1000

DNA_SIZE = len(TARGET_PHRASE)
TARGET_ASCII = np.fromstring(TARGET_PHRASE,dtype=np.uint8)
ASCII_BOUND = [32,126]

class GA:
    def __init__(self,DNA_size,DNA_bound,cross_rate,mutation_rate,pop_size):
        self.DNA_size = DNA_size
        self.DNA_bound = DNA_bound
        self.cross_rate = cross_rate
        self.mutaton_rate = mutation_rate
        self.pop_size = pop_size

    def translateDNA(self,DNA):
        pass

    def get_fitness(self):
        pass

    def select(self):
        fitness = self.get_fitness()+1e-4
        pass

    def crossover(self,parent,pop):
        if np.random.rand()<self.cross_rate:
            i_ = np.random.randint(0,self.pop_size,size=1)
            cross_points = np.random.randint(0,2,
                            self.DNA_size.astype(np.bool))
            parent[cross_points] =  pop[i_,cross_points]
        return parent

    def mutate(self,child):
        for point in range(self.DNA_size):
            if np.random.rand()<self.mutaton_rate:
                child[point] = np.random.randint(*self.DNA_bound)
        return child

    def evolve(self):
        pass

if __name__ == '__main__':
    ga = GA(DNA_size=DNA_SIZE,DNA_bound=ASCII_BOUND,
            cross_rate=CROSS_RATE,mutation_rate=MUTATION_RATE,
            pop_size=POP_SIZE)
    for generation in range(N_GENERATIONS):
        fitness = ga.get_fitness()
        best_DNA = ga.pop[np.argmax(fitness)]
        best_phrase = ga.translateDNA(best_DNA)
        print('Gen',generation,':',best_phrase)
        if best_phrase == TARGET_PHRASE:
            break
        ga.evolve()


